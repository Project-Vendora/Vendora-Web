from flask import request, render_template, redirect, url_for, Blueprint, flash
from vendora_app.blueprints.vendor.models import Vendor
from flask_login import login_user, logout_user, current_user, login_required
from vendora_app.app import db

vendor = Blueprint('vendor', __name__, template_folder = 'templates')

@vendor.route('/')
def index():
    return render_template('vendor/index.html')

@vendor.route('/profile_setup', methods = ['GET','POST'])
@login_required
def profile_setup():
    if request.method == 'GET':
        return render_template('vendor/profile_setup.html')
    
    shop_name = request.form.get('shop_name')
    gst_number = request.form.get('gst_number')
    business_address = request.form.get('business_address')
    
    if current_user.vendor_profile:
        flash('Profile already exists','info')
        return redirect(url_for('vendor.dashboard'))
    
    new_profile = Vendor(
        user_id = current_user.uid,
        shop_name = shop_name,
        gst_number = gst_number,
        business_address = business_address
    )
    
    db.session.add(new_profile)
    db.session.commit()
    
    flash('Vendor Profile completed successfully!', 'Success')
    return redirect(url_for('vendor.dashboard'))


@vendor.route('/dashboard')
@login_required
def dashboard():
    if current_user.is_vendor != True:
        return "Access denied", 403
    
    """if current_user.last_role == 'customer':
        return "Access denied", 403"""
    
    vendor = current_user.vendor_profile
    return render_template('vendor/dashboard.html',vendor=vendor)

    """
    Can Access the information using
    <h2>{{ vendor.shop_name }}</h2>
    <p>Business type: {{ vendor.business_type }}</p>
    """



"""
@vendor.route('/dashboard1')
def dashboard():
    return render_template('vendor/dashboard.html')
"""
    

@vendor.route('/edit_business')
def edit_business():
    return render_template('vendor/dashboard.html')

@vendor.route('/appointments')
def appointments():
    return render_template('vendor/dashboard.html')

@vendor.route('/analytics')
def analytics():
    return render_template('vendor/dashboard.html')

@vendor.route('/reviews')
def reviews():
    return render_template('vendor/dashboard.html')

@vendor.route('/support')
def support():
    return render_template('vendor/dashboard.html')