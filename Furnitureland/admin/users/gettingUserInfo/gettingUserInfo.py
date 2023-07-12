from flask import Blueprint, render_template, session, request
from pymongo import MongoClient
import os

DATABASE_URL = os.getenv('DATABASE_URL')
gettingUserInfo_page = Blueprint('gettingUserInfo_page', __name__, template_folder='templates')

cluster = MongoClient(DATABASE_URL, tls=True, tlsAllowInvalidCertificates=True)
db = cluster["Cluster"]

# Getting user order collection
userOrders = db['userOrders']

@gettingUserInfo_page.route('/gettingUserInfo', methods=['POST', 'GET'])
def gettingUserInfo():
        all_userOrders = userOrders.find()

        return render_template('editUsersOrders.html',all_userOrders=all_userOrders)
