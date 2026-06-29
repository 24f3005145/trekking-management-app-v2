from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.models.trek import Trek
from app.models.booking import Booking
from app.extensions import db
from app.utils.decorators import role_required

user_bp = Blueprint("user", __name__)

@user_bp.route("/treks", methods=["GET"])
@jwt_required()
def get_available_treks():

    treks = Trek.query.filter_by(status="Open").all()

    result = []

    for t in treks:
        result.append({
            "id": t.id,
            "name": t.name,
            "location": t.location,
            "difficulty": t.difficulty,
            "duration": t.duration,
            "available_slots": t.available_slots
        })

    return jsonify(result)

@user_bp.route("/book/<int:trek_id>", methods=["POST"])
@role_required("Trekker")
def book_trek(trek_id):

    user_id = get_jwt_identity()

    trek = Trek.query.get_or_404(trek_id)

    # Check status
    if trek.status != "Open":
        return jsonify({"message": "Trek not open"}), 400

    # Check slots
    if trek.available_slots <= 0:
        return jsonify({"message": "No slots available"}), 400

    # Check duplicate booking
    existing = Booking.query.filter_by(
        user_id=user_id,
        trek_id=trek_id
    ).first()

    if existing:
        return jsonify({"message": "Already booked"}), 400

    booking = Booking(
        user_id=user_id,
        trek_id=trek_id,
        status="Booked"
    )

    trek.available_slots -= 1

    db.session.add(booking)
    db.session.commit()

    return jsonify({"message": "Trek booked successfully"}), 201

@user_bp.route("/bookings", methods=["GET"])
@role_required("Trekker")
def user_bookings():

    user_id = get_jwt_identity()

    bookings = Booking.query.filter_by(user_id=user_id).all()

    result = []

    for b in bookings:
        result.append({
            "booking_id": b.id,
            "trek_name": b.trek.name,
            "location": b.trek.location,
            "status": b.status,
            "booking_date": b.booking_date
        })

    return jsonify(result)












