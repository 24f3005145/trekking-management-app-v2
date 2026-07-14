# IMPORTS ================================================================================================================
from flask import (Blueprint, jsonify, request, send_from_directory, current_app)       # Flask

from flask_jwt_extended import jwt_required, get_jwt_identity                           # Authentication

from werkzeug.security import generate_password_hash                                    # Password Utilities

from app.extensions import db, cache                                                    # Application Extensions

from app.models.trek import Trek                                                        # Models
from app.models.booking import Booking
from app.models.export_job import ExportJob
from app.models.user import User

from app.utils.decorators import role_required                                          # Utilities
# from app.tasks.exports import export_booking_history

# Blueprint =============================================================================================================
user_bp = Blueprint("user", __name__)


# Cache Helpers =========================================================================================================
# Uses cache version so all cached trek listings, can be invalidated by incrementing one value.
def generate_trek_cache_key(search, difficulty, location, duration):     
                                                                                
    version = cache.get("treks_cache_version")

    if version is None:
        version = 1
        cache.set("treks_cache_version", version)

    return (
        f"treks:v{version}:"
        f"{search}:"
        f"{difficulty}:"
        f"{location}:"
        f"{duration}"
    )

# Trek Discovery ========================================================================================================
@user_bp.route("/treks", methods=["GET"])
@jwt_required()
@role_required("Trekker")
def get_available_treks():

    # ---------------------------------------------------------
    # Trek Search & Filter Parameters
    # All filters are optional.
    # Example:  /user/treks?search=valley&difficulty=Easy
    # ---------------------------------------------------------

    search = request.args.get("search", "").strip()
    difficulty = request.args.get("difficulty", "").strip()
    location = request.args.get("location", "").strip()
    duration = request.args.get("duration", type=int)

    # ---------------------------------------------------------
    # Check Redis cache before querying the database.
    # ---------------------------------------------------------

    cache_key = generate_trek_cache_key(
        search,
        difficulty,
        location,
        duration
    )

    cached_result = cache.get(cache_key)

    if cached_result is not None:
        return jsonify(cached_result)

    # ---------------------------------------------------------
    # Base Query
    # Only show treks that are currently open.
    # ---------------------------------------------------------

    query = Trek.query.filter_by(status="Open")

    # ---------------------------------------------------------
    # Apply Search Filter
    # Search by trek name (case-insensitive).
    # ---------------------------------------------------------

    if search:
        query = query.filter(Trek.name.ilike(f"%{search}%"))

    # ---------------------------------------------------------
    # Apply Difficulty Filter
    # ---------------------------------------------------------

    if difficulty:
        query = query.filter(Trek.difficulty == difficulty)

    # ---------------------------------------------------------
    # Apply Location Filter
    # ---------------------------------------------------------

    if location:
        query = query.filter(Trek.location.ilike(f"%{location}%"))

    # ---------------------------------------------------------
    # Apply Duration Filter
    # Exact number of trekking days.
    # ---------------------------------------------------------

    if duration is not None:
        query = query.filter(Trek.duration == duration)

    # ---------------------------------------------------------
    # Execute Query
    # ---------------------------------------------------------

    treks = query.all()

    result = []

    # ---------------------------------------------------------
    # Prepare JSON Response
    # ---------------------------------------------------------

    for t in treks:
        result.append({
            "id": t.id,
            "name": t.name,
            "location": t.location,
            "difficulty": t.difficulty,
            "duration": t.duration,
            "available_slots": t.available_slots
        })

    # ---------------------------------------------------------
    # Store the response in Redis before returning it.
    # ---------------------------------------------------------

    cache.set(cache_key, result)

    return jsonify(result)

@user_bp.route("/treks/<int:trek_id>", methods=["GET"])
@jwt_required()
def get_trek_details(trek_id):            # Get Complete Details of a Single Trek, Used by the Trek Details page.

    # ---------------------------------------------------------
    # Fetch the requested trek or return 404 if it does not exist.
    # ---------------------------------------------------------
    trek = Trek.query.get_or_404(trek_id)

    # ---------------------------------------------------------
    # Prepare response with complete trek details.
    # If no staff is assigned, return None.
    # ---------------------------------------------------------
    result = {
        "id": trek.id,
        "name": trek.name,
        "location": trek.location,
        "difficulty": trek.difficulty,
        "duration": trek.duration,
        "status": trek.status,
        "available_slots": trek.available_slots,
        "start_date": trek.start_date.isoformat() if trek.start_date else None,
        "end_date": trek.end_date.isoformat() if trek.end_date else None,
        "assigned_staff": trek.staff.name if trek.staff else None,
        "description": trek.description
    }

    return jsonify(result)


# Trek Booking ==========================================================================================================
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
def user_bookings():                    # Get Logged-in User's Bookings, Used for My Bookings and Trek History pages.

    # ---------------------------------------------------------
    # Get the logged-in Trekker's ID.
    # ---------------------------------------------------------
    user_id = get_jwt_identity()

    # ---------------------------------------------------------
    # Fetch all bookings for the logged-in user.
    # ---------------------------------------------------------
    bookings = Booking.query.filter_by(user_id=user_id).all()

    result = []

    # ---------------------------------------------------------
    # Prepare booking details with trek information.
    # ---------------------------------------------------------
    for b in bookings:
        result.append({
            "booking_id": b.id,
            "trek_name": b.trek.name,
            "location": b.trek.location,
            "difficulty": b.trek.difficulty,
            "duration": b.trek.duration,
            "start_date": b.trek.start_date.isoformat() if b.trek.start_date else None,
            "end_date": b.trek.end_date.isoformat() if b.trek.end_date else None,
            "status": b.status,
            "payment_status": b.payment_status,
            "available_slots": b.trek.available_slots,
            "booking_date": b.booking_date.isoformat()
        })

    return jsonify(result)


# Booking Export ========================================================================================================
@user_bp.route("/export-bookings", methods=["POST"])
@role_required("Trekker")
def export_bookings():                  # Start asynchronous booking history export.

    user_id = int(get_jwt_identity())

    # ---------------------------------------------------------
    # Create export job.
    # ---------------------------------------------------------

    job = ExportJob(
        user_id=user_id,
        status="Pending"
    )

    db.session.add(job)
    db.session.commit()

    # ---------------------------------------------------------
    # Queue Celery task.
    # ---------------------------------------------------------

    from app.tasks.exports import export_booking_history
    task = export_booking_history.delay(job.id)

    # ---------------------------------------------------------
    # Save Celery task id.
    # ---------------------------------------------------------

    job.task_id = task.id

    db.session.commit()

    return jsonify({

        "message": "Export started successfully",

        "job_id": job.id,

        "task_id": task.id

    }), 202

@user_bp.route("/export-status/<int:job_id>", methods=["GET"])
@role_required("Trekker")
def export_status(job_id):              # Get export job status.

    user_id = int(get_jwt_identity())

    job = ExportJob.query.filter_by(
        id=job_id,
        user_id=user_id
    ).first_or_404()

    return jsonify({

        "job_id": job.id,

        "status": job.status,

        "filename": job.filename,

        "download_url": (
            f"/api/user/download-export/{job.id}"
            if job.status == "Completed"
            else None
        ),

        "completed_at": (
            job.completed_at.isoformat()
            if job.completed_at
            else None
        )

    })

@user_bp.route("/download-export/<int:job_id>", methods=["GET"])
@role_required("Trekker")
def download_export(job_id):            # Download completed export.

    user_id = int(get_jwt_identity())

    job = ExportJob.query.filter_by(
        id=job_id,
        user_id=user_id
    ).first_or_404()

    if job.status != "Completed":

        return jsonify({

            "message": "Export is not ready yet."

        }), 400

    return send_from_directory(

        current_app.config["EXPORT_FOLDER"],

        job.filename,

        as_attachment=True

    )



# User Profile===========================================================================================================
@user_bp.route("/profile", methods=["GET"])
@role_required("Trekker")
def get_profile():                     # NEW: Get logged-in user's profile

    user_id = int(get_jwt_identity())

    user = User.query.get_or_404(user_id)

    return jsonify({

        "id": user.id,
        "name": user.name,
        "email": user.email,
        "phone": user.phone

    })

@user_bp.route("/profile", methods=["PUT"])
@role_required("Trekker")
def update_profile():                  # NEW: Update logged-in user's profile

    user_id = int(get_jwt_identity())

    user = User.query.get_or_404(user_id)

    data = request.get_json()

    user.name = data.get("name", user.name)
    user.phone = data.get("phone", user.phone)

    db.session.commit()

    return jsonify({

        "message": "Profile updated successfully"

    })

@user_bp.route("/change-password", methods=["PUT"])
@role_required("Trekker")
def change_password():                 # NEW: Change logged-in user's password

    user_id = int(get_jwt_identity())

    user = User.query.get_or_404(user_id)

    data = request.get_json()

    current_password = data.get("current_password")
    new_password = data.get("new_password")

    # -------------------------------------------------
    # Validate current password
    # -------------------------------------------------

    if not user.check_password(current_password):

        return jsonify({

            "message": "Current password is incorrect"

        }), 400

    user.password = generate_password_hash(new_password)

    db.session.commit()

    return jsonify({

        "message": "Password changed successfully"

    })





