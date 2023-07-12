from flask import Blueprint, render_template

editUsers_page = Blueprint('editUsers_page', __name__, template_folder='templates')


@editUsers_page.route('/editUsers', methods=['POST', 'GET'])
def editUsers():

    return render_template('editUsers.html' )
