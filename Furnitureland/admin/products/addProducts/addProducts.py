from flask import Blueprint, render_template, request, flash
from pymongo import MongoClient
import os

DATABASE_URL = os.getenv('DATABASE_URL')
addProducts_page = Blueprint('addProducts_page', __name__, template_folder='templates')

cluster = MongoClient(DATABASE_URL, tls=True, tlsAllowInvalidCertificates=True)
db = cluster["Cluster"]

# Getting products collection
products = db['products']

def store_product(ProductName, ProductInfo, ProductPrice):
    product = {"product_name": ProductName, "product_info": ProductInfo, "product_price": ProductPrice}
    products.insert_one(product)


@addProducts_page.route('/addProducts', methods=['POST', 'GET'])
def addProducts():
    if request.method == "POST":
        product_name = request.form['product_name']
        product_info = request.form['product_info']
        product_price = request.form['product_price']

        existing_product = products.find_one({"product_name": product_name})
        
        if product_name != None and product_info != None and product_price != None:
            if existing_product is None:
                store_product(product_name, product_info, product_price)
                flash('Product stored successfully', 'success')
            else: 
                flash('Storing failed - product already exists in the database.', 'error')
        else: 
            flash('Please enter all field', 'error')


    return render_template('addProducts.html')  
