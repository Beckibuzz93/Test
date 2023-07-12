from flask import Blueprint, render_template, redirect, url_for, session

adminDashboard_page = Blueprint('adminDashboard_page', __name__, template_folder='templates')

@adminDashboard_page.route('/adminDashboard', methods=['POST', 'GET'])
def adminDashboard():
    try:
        if session['email'] is None:
            return redirect(url_for('adminLogin_page.adminLogin'))
        else:
            return render_template('adminDashboard.html')  
    except: 
        return redirect(url_for('adminLogin_page.adminLogin'))
