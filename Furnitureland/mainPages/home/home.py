from flask import Blueprint, render_template, session

home_page = Blueprint('home_page', __name__, template_folder='templates')

from pymongo import MongoClient
import os

DATABASE_URL = os.getenv('DATABASE_URL')

cluster = MongoClient(DATABASE_URL, tls=True, tlsAllowInvalidCertificates=True)
db = cluster["Cluster"]

# Getting user collection
users = db['users']


@home_page.route('/')
@home_page.route('/index')
def index():
    return render_template('index.html')  
