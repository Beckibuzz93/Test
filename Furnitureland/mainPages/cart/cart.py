from flask import Blueprint, render_template, redirect, url_for, flash, session, request
from pymongo import MongoClient
import random
import os

DATABASE_URL = os.getenv('DATABASE_URL')
cart_page = Blueprint('cart_page', __name__, template_folder='templates')

cluster = MongoClient(DATABASE_URL, tls=True, tlsAllowInvalidCertificates=True)
db = cluster["Cluster"]

# Getting user collection
users = db['users']

# Getting products collection
products = db['products']

# Getting tempStore collection
tempStore = db['tempStore']

# Getting userOrders collection
userOrders = db['userOrders']

def store_order(OrderNumber, Email, ProductName, ProductPrice, OrderTrack):
    userOrder = {"order_number": OrderNumber,"email": Email, "product_name": ProductName, "product_price": ProductPrice, "order_track": OrderTrack}
    userOrders.insert_one(userOrder)


@cart_page.route('/cart', methods=['POST', 'GET'])
def cart():
    all_temp_products = tempStore.find()
    email = session['email']

    try: 
        if session['email'] is None:
                flash('Please log in before you add items to your cart', 'error')
        else:
            if request.method == 'POST':
                temp_products = tempStore.find()

                for all_items in temp_products:
                    order_number = all_items['order_number']
                    product_name = all_items['product_name']
                    product_price = all_items['product_price']
                    order_track = "Getting ready for dispatch"
                    
                    store_order(order_number, email, product_name, product_price, order_track)
                
                    query = {"email": email, "product_name": product_name}
                    x = tempStore.delete_one(query)
                    print(x.deleted_count, "documents deleted")

                flash('Your items have been ordered, Thank you', 'success')

    except:
        return redirect(url_for('login_page.login'))

    return render_template('cart.html', all_temp_products=all_temp_products)  

