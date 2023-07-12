from flask import Blueprint, render_template, session, redirect, url_for
from pymongo import MongoClient
import os

DATABASE_URL = os.getenv('DATABASE_URL')

userAccount_page = Blueprint('userAccount_page', __name__, template_folder='templates')
cluster = MongoClient(DATABASE_URL, tls=True, tlsAllowInvalidCertificates=True)
db = cluster["Cluster"]
# Getting user collection
users = db['users']

@userAccount_page.route('/userAccount')
def userAccount():
        try:
            if session['email'] is None:
                return redirect(url_for('login_page.login'))
            else:
                user_session_email = session['email']
                for user_info in users.find({"email": user_session_email}):
                    user_email = user_info["email"]
                    user_fname = user_info["fname"]
                    user_lname = user_info['lname']
                    return render_template('userAccount.html', user_email=user_email, user_fname=user_fname, user_lname=user_lname)  
        except: 
            return redirect(url_for('login_page.login'))

