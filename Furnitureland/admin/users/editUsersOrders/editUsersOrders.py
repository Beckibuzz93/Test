from flask import Blueprint, render_template, request, redirect, url_for, flash
from pymongo import MongoClient
import os

DATABASE_URL = os.getenv('DATABASE_URL')
editUsersOrders_page = Blueprint('editUsersOrders_page', __name__, template_folder='templates')

cluster = MongoClient(DATABASE_URL, tls=True, tlsAllowInvalidCertificates=True)
db = cluster["Cluster"]

# Getting user order collection
usersOrders = db['userOrders']

@editUsersOrders_page.route('/editUsersOrders', methods=['POST', 'GET'])
def editUsersOrders():
    if request.method == 'POST':
        order_number = request.form['order_number']
        email = request.form['email']
        product_name = request.form['product_name']
        product_price = request.form['product_price']
        order_track = request.form['order_track']

        print(email, product_name, product_price, order_track)

        #Order does not update currently
        cursor = usersOrders.update_one({"order_number": order_number}, {"$set": {"order_track": order_track}})

        print(cursor)
        

        flash('Order updated succesfully', 'success')
        return render_template('editUsersOrders.html')

