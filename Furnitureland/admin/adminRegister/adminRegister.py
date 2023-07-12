from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash
from pymongo import MongoClient
from validate_email import validate_email
import os

DATABASE_URL = os.getenv('DATABASE_URL')

adminRegister_page = Blueprint('adminRegister_page', __name__, template_folder='templates')
cluster = MongoClient(DATABASE_URL, tls=True, tlsAllowInvalidCertificates=True)
db = cluster["Cluster"]
# Getting admin user collection
admin_user = db['admin']

def store_user(Email, Password, Fname, Lname):
    user = {"email": Email, "password": Password, "fname": Fname, "lname": Lname}
    admin_user.insert_one(user)


@adminRegister_page.route('/adminRegister', methods=['POST', 'GET'])
def adminRegister():
    #Registering a user and adding them to the database
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        fname = request.form['fname']
        lname = request.form['lname']

        is_email_valid = validate_email(email)
        existing_user = admin_user.find_one({'email': email})

        if existing_user is None and is_email_valid == True:
            password_hash = generate_password_hash(password)
            email.upper()
            store_user(email, password_hash, fname, lname)
            flash('Admin account created, they can now log in.', 'success')
        elif is_email_valid == False:
            flash('That Email does not exist, please use a valid email.', 'error')
        else: 
           flash('That admin account name already exists, please log in instead.', 'error')
    return render_template('adminRegister.html')  
