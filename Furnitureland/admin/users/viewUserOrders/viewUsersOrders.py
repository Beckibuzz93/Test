from flask import Blueprint, render_template
from pymongo import MongoClient
import os

DATABASE_URL = os.getenv('DATABASE_URL')
viewUsersOrders_page = Blueprint('viewUsersOrders_page', __name__, template_folder='templates')

cluster = MongoClient(DATABASE_URL, tls=True, tlsAllowInvalidCertificates=True)
db = cluster["Cluster"]
# Getting user order collection
userOrders = db['userOrders']


@viewUsersOrders_page.route('/viewUsersOrders', methods=['POST', 'GET'])
def viewUsersOrders():
    all_userOrders = userOrders.find()

    return render_template('viewUsersOrders.html', all_userOrders=all_userOrders)
