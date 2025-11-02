
from vendora_app.app import db
from flask_login import UserMixin
from datetime import datetime


class Vendor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.uid'), nullable=False)
    shop_name = db.Column(db.String(100))
    gst_number = db.Column(db.String(20))
    business_address = db.Column(db.String(200))
    # add other vendor-specific fields
    # --- Relationships ---
    # Example relationship for Addresses (assuming an 'Addresses' model exists)
    # addresses = db.relationship('Address', backref='vendor', lazy='dynamic')
    