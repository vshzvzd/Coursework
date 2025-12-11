from flask import Blueprint, request, jsonify
from models import db, User, InventoryItem, InventoryCheck, InventoryCheckDetail, LogEntry

main_bp = Blueprint('main', __name__)

@main_bp.route("/users", methods=["GET"])
def get_users():
    users = User.query.all()
    return jsonify([{"id": u.id, "name": u.first_name + " " + u.last_name, "role": u.role} for u in users])

@main_bp.route("/items", methods=["GET"])
def get_items():
    items = InventoryItem.query.all()
    return jsonify([{"id": i.id, "name": i.name, "status": i.status} for i in items])

@main_bp.route("/logs", methods=["GET"])
def get_logs():
    logs = LogEntry.query.all()
    return jsonify([{"id": l.id, "user_id": l.user_id, "action": l.action} for l in logs])
