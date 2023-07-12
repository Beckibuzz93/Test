from flask import Blueprint, render_template, request, flash, session, redirect, url_for
from pymongo import MongoClient
import random
import os

DATABASE_URL = os.getenv('DATABASE_URL')
products_page = Blueprint('products_page', __name__, template_folder='templates')

cluster = MongoClient(DATABASE_URL, tls=True, tlsAllowInvalidCertificates=True)
db = cluster["Cluster"]

# Getting user collection
users = db['users']

# Getting products collection
product = db['products']

# Getting tempStore collection
tempStore = db['tempStore']

def store_item_temp(Item, Price):
    items = {"product_name": Item, 'product_price': Price}
    tempStore.insert_one(items)

def store_item_temp(Email, ProductName, ProductPrice, OrderTrack, OrderNumber):
    items = {"email": Email, "product_name": ProductName, "product_price": ProductPrice, "order_track": OrderTrack, "order_number": OrderNumber}
    tempStore.insert_one(items)

@products_page.route('/products', methods=['POST', 'GET'])
def products():
    all_products = product.find()

    if request.method == 'POST':
        product_name = request.form['product_name']
        product_price = request.form['product_price']

    try: 
        email = session['email']
        if session['email'] != None:
            order_track = "Getting ready for dispatch"
            order_number = (random.randint(0, 1000000000))
            store_item_temp(email, product_name, product_price, order_track, order_number)
            flash('Added to cart', 'info')
    except:
        flash('Please log in before you add items to your cart', 'error')
    
    return render_template('products.html', all_products=all_products)


