from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required

from app.utils.decorators import role_required

dashboard_bp = Blueprint("dashboard", __name__)


@dashboard_bp.route("/admin")
@role_required("Admin")
def admin_dashboard():
    return jsonify({
        "message": "Welcome Admin"
    })


@dashboard_bp.route("/staff")
@role_required("Trek Staff")
def staff_dashboard():
    return jsonify({
        "message": "Welcome Trek Staff"
    })


@dashboard_bp.route("/trekker")
@role_required("Trekker")
def trekker_dashboard():
    return jsonify({
        "message": "Welcome Trekker"
    })