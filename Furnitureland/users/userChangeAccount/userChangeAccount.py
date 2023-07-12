from flask import Blueprint, render_template, session, request, flash, redirect, url_for
from pymongo import MongoClient
import os

DATABASE_URL = os.getenv('DATABASE_URL')

userChangeAccount_page = Blueprint('userChangeAccount_page', __name__,template_folder='templates')
cluster = MongoClient(DATABASE_URL, tls=True, tlsAllowInvalidCertificates=True)
db = cluster["Cluster"]
# Getting user collection
users = db['users']


@userChangeAccount_page.route('/userChangeAccount', methods = ['GET', 'POST'])
def userChangeAccount():
    user_session_email = session['email']
    for user_info in users.find({"email": user_session_email}):
        user_fname = user_info["fname"]
        user_lname = user_info['lname']

    if request.method == "POST":
        email = request.form['email']
        fname = request.form['fname']
        lname = request.form['lname']
        if fname != user_fname or lname != user_lname:
            if fname != "":
                users.find_one_and_update(
                    {"email": user_session_email},
                    {"$set": {"fname": fname}},
                    new=True
                )
            if lname != "":
                users.find_one_and_update(
                    {"email": user_session_email},
                    {"$set": {"lname": lname}},
                    new=True
                )
            if email != "":
                users.find_one_and_update(
                    {"email": user_session_email},
                    {"$set": {"email": email}},
                    new=True
                )
                session['email'] = email
            return redirect(url_for('userAccount_page.userAccount'))
        else: 
            flash('Account details are the same!', 'error')
    return render_template('userChangeAccount.html', user_session_email=user_session_email)  
