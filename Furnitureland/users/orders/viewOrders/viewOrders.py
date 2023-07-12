from flask import Blueprint, render_template, session, redirect, url_for, request
from pymongo import MongoClient
import os

DATABASE_URL = os.getenv('DATABASE_URL')

viewOrders_page = Blueprint('viewOrders_page', __name__, template_folder='templates')

cluster = MongoClient(DATABASE_URL, tls=True, tlsAllowInvalidCertificates=True)
db = cluster["Cluster"]

# Getting user orders collection
userOrders = db['userOrders']

# Getting user collection
users = db['users']

@viewOrders_page.route('/viewOrders', methods=['POST', 'GET'])
def viewOrders():
    try:
        if session['email'] is None:
            return redirect(url_for('login_page.login'))
        else:
            user = userOrders.find({"email": session['email']})
            return render_template('viewOrders.html', user=user)
    except: 
        return redirect(url_for('login_page.login'))
