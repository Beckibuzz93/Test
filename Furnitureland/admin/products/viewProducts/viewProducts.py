from flask import Blueprint, render_template
from pymongo import MongoClient
import os

DATABASE_URL = os.getenv('DATABASE_URL')

viewProducts_page = Blueprint('viewProducts_page', __name__, template_folder='templates')
cluster = MongoClient(DATABASE_URL, tls=True, tlsAllowInvalidCertificates=True)
db = cluster["Cluster"]
# Getting user collection
products = db['products']

@viewProducts_page.route('/viewProducts', methods=['POST', 'GET'])
def viewUsers():
    every_product = products.find()
    
    return render_template('viewProducts.html', every_product=every_product )  
