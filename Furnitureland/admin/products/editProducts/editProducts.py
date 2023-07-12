from flask import Blueprint, render_template


editProducts_page = Blueprint('editProducts_page', __name__, template_folder='templates')



@editProducts_page.route('/editProducts', methods=['POST', 'GET'])
def editProducts():

    return render_template('editProducts.html')  