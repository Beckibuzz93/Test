from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from werkzeug.security import check_password_hash
from pymongo import MongoClient
import os

DATABASE_URL = os.getenv('DATABASE_URL')

adminLogin_page = Blueprint('adminLogin_page', __name__, template_folder='templates')
cluster = MongoClient(DATABASE_URL, tls=True, tlsAllowInvalidCertificates=True)
db = cluster["Cluster"]
# Getting admin user collection
admin_users = db['admin']

@adminLogin_page.route('/adminLogin', methods=['POST', 'GET'])
def adminLogin():
    #Log in function 
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        email.upper()
        existing_user = admin_users.find_one({'email': email})

        if existing_user:
            if check_password_hash(existing_user['password'], password):
                session['email'] = email
                return redirect(url_for('adminDashboard_page.adminDashboard'))
            else: 
                flash('Login failed - The username or password entered is incorrect', 'error')
        else: 
            flash('Login failed - That user does not exist, please register instead', 'error')

    return render_template('adminLogin.html')  
