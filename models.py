from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    role = db.Column(db.String(50))
    login = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    inventory_items = db.relationship('InventoryItem', backref='responsible_user', lazy=True)
    inventory_checks = db.relationship('InventoryCheck', backref='responsible_user', lazy=True)
    log_entries = db.relationship('LogEntry', backref='user', lazy=True)

class InventoryItem(db.Model):
    __tablename__ = 'inventory_items'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    category = db.Column(db.String(50))
    cost = db.Column(db.Float)
    received_date = db.Column(db.DateTime)
    status = db.Column(db.String(50))
    location = db.Column(db.String(100))
    responsible_user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

class InventoryCheck(db.Model):
    __tablename__ = 'inventory_checks'
    id = db.Column(db.Integer, primary_key=True)
    check_date = db.Column(db.DateTime, default=datetime.utcnow)
    responsible_user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    details = db.relationship('InventoryCheckDetail', backref='inventory_check', lazy=True)

class InventoryCheckDetail(db.Model):
    __tablename__ = 'inventory_check_details'
    check_id = db.Column(db.Integer, db.ForeignKey('inventory_checks.id'), primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey('inventory_items.id'), primary_key=True)
    actual_status = db.Column(db.String(50))
    discrepancy = db.Column(db.String(100))

class LogEntry(db.Model):
    __tablename__ = 'log_entries'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    action = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
