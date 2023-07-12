from flask import Blueprint, render_template
from pymongo import MongoClient
import os

DATABASE_URL = os.getenv('DATABASE_URL')
viewUsers_page = Blueprint('viewUsers_page', __name__, template_folder='templates')
cluster = MongoClient(DATABASE_URL, tls=True, tlsAllowInvalidCertificates=True)
db = cluster["Cluster"]
# Getting user collection
users = db['users']

@viewUsers_page.route('/viewUsers', methods=['POST', 'GET'])
def viewUsers():
    all_users = users.find()
    
    return render_template('viewUsers.html', all_users=all_users)  
