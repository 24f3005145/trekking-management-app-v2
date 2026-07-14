# IMPORTS ================================================================================================================
from flask import Blueprint, jsonify, request                         # Flask
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.extensions import db, cache                                  # Application Extensions

from app.models.trek import Trek                                      # Models
from app.models.booking import Booking
from app.models.user import User

from app.utils.decorators import role_required                        # Utilities

# Blueprints ================================================================================================================
staff_bp = Blueprint("staff", __name__)


# Allowed Trek Statuses=====================================================================================================
ALLOWED_TREK_STATUSES = {
    "Pending",
    "Open",
    "Upcoming",
    "Completed"
}

# Cache Helpers ===========================================================================================================
def invalidate_trek_cache():                    # Invalidate all cached trek listings, by incrementing the cache version.

    version = cache.get("treks_cache_version")

    if version is None:
        version = 1

    cache.set("treks_cache_version", version + 1)


# Dashboard route =========================================================================================================
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

# Assigned Trek Management routes =========================================================================================
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

    invalidate_trek_cache()

    return jsonify({"message": "Slots updated"})

@staff_bp.route("/trek/<int:trek_id>/status", methods=["PUT"])
@role_required("Trek Staff")
def update_status(trek_id):

    data = request.get_json()

    trek = Trek.query.get_or_404(trek_id)

    user_id = int(get_jwt_identity())

    if trek.assigned_staff_id != user_id:
        return jsonify({"message": "Not assigned to this trek"}), 403

    new_status = data.get("status")

    if new_status not in ALLOWED_TREK_STATUSES:
        return jsonify({
            "message": "Invalid trek status."
        }), 400

    trek.status = new_status

    db.session.commit()

    invalidate_trek_cache()

    return jsonify({
        "message": "Status updated"
    })

# Participant Management ==================================================================================================
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
            "booking_id": b.id,
            "user_id": b.user.id,
            "user_name": b.user.name,
            "email": b.user.email,
            "phone": b.user.phone,
            "booking_date": (
                b.booking_date.strftime("%Y-%m-%d")
                if b.booking_date else None
            ),
            "booking_status": b.status,
            "payment_status": b.payment_status
        })

    return jsonify(result)

@staff_bp.route("/booking/<int:booking_id>/status", methods=["PUT"])
@role_required("Trek Staff")
def update_booking_status(booking_id):

    booking = Booking.query.get_or_404(booking_id)

    user_id = int(get_jwt_identity())

    if booking.trek.assigned_staff_id != user_id:

        return jsonify({
            "message": "Not assigned to this trek."
        }), 403

    data = request.get_json()

    allowed_statuses = {

        "Booked",

        "Checked In",

        "Completed",

        "Cancelled"

    }

    status = data.get("status")

    if status not in allowed_statuses:

        return jsonify({
            "message": "Invalid booking status."
        }), 400

    booking.status = status

    db.session.commit()

    return jsonify({
        "message": "Booking status updated successfully."
    })

@staff_bp.route("/booking/<int:booking_id>", methods=["DELETE"])
@role_required("Trek Staff")
def remove_participant(booking_id):

    booking = Booking.query.get_or_404(booking_id)

    user_id = int(get_jwt_identity())

    trek = booking.trek

    if trek.assigned_staff_id != user_id:

        return jsonify({
            "message": "Not assigned to this trek."
        }), 403

    trek.available_slots += 1

    db.session.delete(booking)

    db.session.commit()

    invalidate_trek_cache()

    return jsonify({
        "message": "Participant removed successfully."
    })
















