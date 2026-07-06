from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.models.trek import Trek
from app.models.booking import Booking
from app.models.user import User
from app.extensions import db
from app.utils.decorators import role_required

staff_bp = Blueprint("staff", __name__)

@staff_bp.route("/dashboard", methods=["GET"])
@role_required("Trek Staff")
def dashboard():

    user_id = int(get_jwt_identity())

    staff = User.query.get_or_404(user_id)

    assigned_treks = Trek.query.filter_by(
        assigned_staff_id=user_id
    ).all()

    total = len(assigned_treks)

    upcoming = sum(
        1 for trek in assigned_treks
        if trek.status == "Upcoming"
    )

    completed = sum(
        1 for trek in assigned_treks
        if trek.status == "Completed"
    )

    pending = sum(
        1 for trek in assigned_treks
        if trek.status == "Pending"
    )

    return jsonify({
        "staff": staff.name,
        "assigned_treks": total,
        "upcoming": upcoming,
        "completed": completed,
        "pending": pending
    })

@staff_bp.route("/treks", methods=["GET"])
@role_required("Trek Staff")
def assigned_treks():

    user_id = int(get_jwt_identity())

    treks = Trek.query.filter_by(assigned_staff_id=user_id).all()

    result = []

    for t in treks:
        result.append({
            "id": t.id,
            "name": t.name,
            "location": t.location,
            "status": t.status,
            "available_slots": t.available_slots
        })

    return jsonify(result)

@staff_bp.route("/trek/<int:trek_id>/slots", methods=["PUT"])
@role_required("Trek Staff")
def update_slots(trek_id):

    data = request.get_json()

    trek = Trek.query.get_or_404(trek_id)

    user_id = int(get_jwt_identity())

    if trek.assigned_staff_id != user_id:
        return jsonify({"message": "Not assigned to this trek"}), 403

    trek.available_slots = data.get("available_slots", trek.available_slots)

    db.session.commit()

    return jsonify({"message": "Slots updated"})

@staff_bp.route("/trek/<int:trek_id>/status", methods=["PUT"])
@role_required("Trek Staff")
def update_status(trek_id):

    data = request.get_json()

    trek = Trek.query.get_or_404(trek_id)

    user_id = int(get_jwt_identity())

    if trek.assigned_staff_id != user_id:
        return jsonify({"message": "Not assigned to this trek"}), 403

    trek.status = data.get("status", trek.status)

    db.session.commit()

    return jsonify({"message": "Status updated"})

@staff_bp.route("/trek/<int:trek_id>/participants", methods=["GET"])
@role_required("Trek Staff")
def participants(trek_id):

    trek = Trek.query.get_or_404(trek_id)

    user_id = int(get_jwt_identity())

    if trek.assigned_staff_id != user_id:
        return jsonify({"message": "Not assigned"}), 403

    bookings = Booking.query.filter_by(trek_id=trek_id).all()

    result = []

    for b in bookings:
        result.append({
            "user_name": b.user.name,
            "email": b.user.email,
            "status": b.status
        })

    return jsonify(result)

@staff_bp.route("/trek/<int:trek_id>", methods=["GET"])
@role_required("Trek Staff")
def trek_details(trek_id):

    trek = Trek.query.get_or_404(trek_id)

    user_id = int(get_jwt_identity())

    if trek.assigned_staff_id != user_id:
        return jsonify({
            "message": "Not assigned to this trek"
        }), 403

    return jsonify({
        "id": trek.id,
        "name": trek.name,
        "location": trek.location,
        "difficulty": trek.difficulty,
        "duration": trek.duration,
        "start_date": (
            trek.start_date.isoformat()
            if trek.start_date else None
        ),
        "end_date": (
            trek.end_date.isoformat()
            if trek.end_date else None
        ),
        "available_slots": trek.available_slots,
        "status": trek.status
    })














