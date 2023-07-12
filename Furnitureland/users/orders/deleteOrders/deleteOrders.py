from flask import Blueprint, render_template, session, redirect, url_for, request, flash
from pymongo import MongoClient
import os

DATABASE_URL = os.getenv('DATABASE_URL')

deleteOrders_page = Blueprint('deleteOrders_page', __name__, template_folder='templates')

cluster = MongoClient(DATABASE_URL, tls=True, tlsAllowInvalidCertificates=True)
db = cluster["Cluster"]

# Getting user orders collection
userOrders = db['userOrders']

# Getting user collection
users = db['users']

@deleteOrders_page.route('/deleteOrders', methods=['POST', 'GET'])
def deleteOrders():
    email = session['email']
    if request.method == 'POST':
        order_numb = request.form['order_numb']


        userOrders.find_one_and_delete(
                {"email": email},
                {"order_number": order_numb}
            )
            
        flash('Order deleted successfully', 'success')

    return redirect(url_for('viewOrders_page.viewOrders'))
