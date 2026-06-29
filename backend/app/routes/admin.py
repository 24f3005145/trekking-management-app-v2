from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models.trek import Trek
from app.utils.decorators import role_required

from app.models.user import User
from app.models.role import Role

admin_bp = Blueprint("admin", __name__)

@admin_bp.route("/treks", methods=["POST"])
@role_required("Admin")
def create_trek():

    data = request.get_json()

    trek = Trek(
        name=data["name"],
        location=data["location"],
        difficulty=data.get("difficulty"),
        duration=data.get("duration"),
        available_slots=data.get("available_slots", 0),
        status="Open"
    )

    db.session.add(trek)
    db.session.commit()

    return jsonify({"message": "Trek created successfully"}), 201

@admin_bp.route("/treks", methods=["GET"])
@role_required("Admin")
def get_treks():

    treks = Trek.query.all()

    result = []

    for t in treks:
        result.append({
            "id": t.id,
            "name": t.name,
            "location": t.location,
            "difficulty": t.difficulty,
            "duration": t.duration,
            "slots": t.available_slots,
            "status": t.status
        })

    return jsonify(result)

@admin_bp.route("/treks/<int:trek_id>", methods=["PUT"])
@role_required("Admin")
def update_trek(trek_id):

    trek = Trek.query.get_or_404(trek_id)
    data = request.get_json()

    trek.name = data.get("name", trek.name)
    trek.location = data.get("location", trek.location)
    trek.difficulty = data.get("difficulty", trek.difficulty)
    trek.duration = data.get("duration", trek.duration)
    trek.available_slots = data.get("available_slots", trek.available_slots)
    trek.status = data.get("status", trek.status)

    db.session.commit()

    return jsonify({"message": "Trek updated successfully"})

@admin_bp.route("/treks/<int:trek_id>", methods=["DELETE"])
@role_required("Admin")
def delete_trek(trek_id):

    trek = Trek.query.get_or_404(trek_id)

    db.session.delete(trek)
    db.session.commit()

    return jsonify({"message": "Trek deleted successfully"})

@admin_bp.route("/staff", methods=["POST"])
@role_required("Admin")
def create_staff():

    data = request.get_json()

    staff_role = Role.query.filter_by(name="Trek Staff").first()

    if User.query.filter_by(email=data["email"]).first():
        return jsonify({"message": "User already exists"}), 400

    staff = User(
        name=data["name"],
        email=data["email"],
        phone=data.get("phone"),
        role_id=staff_role.id
    )

    staff.set_password(data["password"])

    db.session.add(staff)
    db.session.commit()

    return jsonify({"message": "Staff created successfully"}), 201


@admin_bp.route("/assign-staff/<int:trek_id>", methods=["PUT"])
@role_required("Admin")
def assign_staff(trek_id):

    data = request.get_json()

    trek = Trek.query.get_or_404(trek_id)
    staff = User.query.get_or_404(data["staff_id"])

    if staff.role.name != "Trek Staff":
        return jsonify({"message": "User is not staff"}), 400

    trek.assigned_staff_id = staff.id

    db.session.commit()

    return jsonify({"message": "Staff assigned successfully"})

@admin_bp.route("/staff", methods=["GET"])
@role_required("Admin")
def get_staff():

    staff_role = Role.query.filter_by(name="Trek Staff").first()

    staff_list = User.query.filter_by(role_id=staff_role.id).all()

    result = []

    for s in staff_list:
        result.append({
            "id": s.id,
            "name": s.name,
            "email": s.email,
            "phone": s.phone
        })

    return jsonify(result)


























