from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from werkzeug.security import check_password_hash
from pymongo import MongoClient
import os

DATABASE_URL = os.getenv('DATABASE_URL')

adminAccount_page = Blueprint('adminAccount_page', __name__, template_folder='templates')
cluster = MongoClient(DATABASE_URL, tls=True, tlsAllowInvalidCertificates=True)
db = cluster["Cluster"]
# Getting admin user collection
admin_users = db['admin']

@adminAccount_page.route('/adminAccount', methods=['POST', 'GET'])
def adminAccount():
        try:
            if session['email'] is None:
                return redirect(url_for('adminLogin_page.adminLogin'))
            else:
                user_session_email = session['email']
                for user_info in admin_users.find({"email": user_session_email}):
                    user_email = user_info["email"]
                    user_fname = user_info["fname"]
                    user_lname = user_info['lname']
                    return render_template('adminAccount.html', user_email=user_email, user_fname=user_fname, user_lname=user_lname)  
        except: 
            return redirect(url_for('adminLogin_page.adminLogin')) 
