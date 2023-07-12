from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from pymongo import MongoClient
from werkzeug.security import generate_password_hash
from validate_email import validate_email
import os

DATABASE_URL = os.getenv('DATABASE_URL')

register_page = Blueprint('register_page', __name__, template_folder='templates')
cluster = MongoClient(DATABASE_URL, tls=True, tlsAllowInvalidCertificates=True)
db = cluster["Cluster"]

# Getting user collection
users = db['users']

def store_user(Email, Password, Fname, Lname):
    user = {"email": Email, "password": Password, "fname": Fname, "lname": Lname}
    users.insert_one(user)


@register_page.route('/register', methods=['POST', 'GET'])
def register():
    #Registering a user and adding them to the database
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        fname = request.form['fname']
        lname = request.form['lname']

        is_email_valid = validate_email(email)
        email.upper()
        print(email)
        existing_user = users.find_one({'email': email})

        if existing_user is None and is_email_valid == True:
            password_hash = generate_password_hash(password)
            store_user(email, password_hash, fname, lname)
            session['email'] = email
            return redirect(url_for('userAccount_page.userAccount'))
        elif is_email_valid == False:
            flash('That Email does not exist, please use a valid email.', 'error')
        else: 
            flash('That Account name already exists, please log in instead.', 'error')
 
    return render_template('register.html')  
