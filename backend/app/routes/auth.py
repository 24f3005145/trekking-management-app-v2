from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token

from app.extensions import db
from app.models.user import User
from app.models.role import Role

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():

    data = request.get_json()

    if User.query.filter_by(email=data["email"]).first():
        return jsonify({"message": "Email already exists"}), 400

    trekker_role = Role.query.filter_by(name="Trekker").first()

    user = User(
        name=data["name"],
        email=data["email"],
        phone=data.get("phone"),
        role_id=trekker_role.id
    )

    user.set_password(data["password"])

    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "Registration successful"}), 201

@auth_bp.route("/login", methods=["POST"])
def login():

    data = request.get_json()

    user = User.query.filter_by(
        email=data["email"]
    ).first()

    if not user:
        return jsonify({"message": "Invalid credentials"}), 401

    if not user.check_password(data["password"]):
        return jsonify({"message": "Invalid credentials"}), 401
    
    if not user.is_active:
        return jsonify({
            "message": "Your account has been deactivated. Please contact the administrator."
        }), 403

    token = create_access_token(
        identity=str(user.id),
        additional_claims={
            "role": user.role.name
        }
    )

    return jsonify({
        "token": token,
        "role": user.role.name,
        "user_id": user.id,
        "name": user.name
    })