from flask import Flask
import os

#Main Pages
from mainPages.home.home import home_page
from mainPages.cart.cart import cart_page
from mainPages.products.products import products_page

#Users 
from users.register.register import register_page
from users.login.login import login_page
from users.userAccount.userAccount import userAccount_page
from users.userChangeAccount.userChangeAccount import userChangeAccount_page

#Orders
from users.orders.viewOrders.viewOrders import viewOrders_page
from users.orders.deleteOrders.deleteOrders import deleteOrders_page

#Admins
from admin.adminRegister.adminRegister import adminRegister_page
from admin.adminLogin.adminLogin import adminLogin_page
from admin.adminAccount.adminAccount import adminAccount_page
from admin.adminDashboard.adminDashboard import adminDashboard_page

from admin.products.addProducts.addProducts import addProducts_page
from admin.products.viewProducts.viewProducts import viewProducts_page
from admin.products.editProducts.editProducts import editProducts_page

from admin.users.viewUsers.viewUsers import viewUsers_page
from admin.users.editUsers.editUsers import editUsers_page
from admin.users.viewUserOrders.viewUsersOrders import viewUsersOrders_page
from admin.users.editUsersOrders.editUsersOrders import editUsersOrders_page
from admin.users.gettingUserInfo.gettingUserInfo import gettingUserInfo_page

app = Flask(__name__)

#Set the apps secret key
SECRET_KEY = os.urandom(64)
app.secret_key = SECRET_KEY


#Main Pages
app.register_blueprint(home_page)
app.register_blueprint(cart_page)
app.register_blueprint(products_page)

#Users 
app.register_blueprint(register_page)
app.register_blueprint(login_page)
app.register_blueprint(userAccount_page)
app.register_blueprint(userChangeAccount_page)

#Orders
app.register_blueprint(viewOrders_page)
app.register_blueprint(deleteOrders_page)

#Admins
app.register_blueprint(adminRegister_page)
app.register_blueprint(adminLogin_page)
app.register_blueprint(adminAccount_page)
app.register_blueprint(adminDashboard_page)

app.register_blueprint(addProducts_page)
app.register_blueprint(viewProducts_page)
app.register_blueprint(editProducts_page)

app.register_blueprint(viewUsers_page)
app.register_blueprint(editUsers_page)
app.register_blueprint(viewUsersOrders_page)
app.register_blueprint(editUsersOrders_page)
app.register_blueprint(gettingUserInfo_page)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)