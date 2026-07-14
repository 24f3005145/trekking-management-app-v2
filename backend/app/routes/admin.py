# IMPORTS ================================================================================================================
from flask import Blueprint, request, jsonify
from app.extensions import db, cache
from app.models.trek import Trek
from app.utils.decorators import role_required

from flask_jwt_extended import get_jwt_identity

from app.models.booking import Booking
from app.models.user import User
from app.models.role import Role

from sqlalchemy import or_

from sqlalchemy import func
from datetime import datetime

# Blueprint ================================================================================================================
admin_bp = Blueprint("admin", __name__)

# Cache Helpers ============================================================================================================

def invalidate_trek_cache():                  # Invalidate all cached trek listings, by incrementing the cache version.

    version = cache.get("treks_cache_version")

    if version is None:
        version = 1

    cache.set("treks_cache_version", version + 1)


# Trek Management routes====================================================================================================
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

    invalidate_trek_cache()

    return jsonify({"message": "Trek created successfully"}), 201

@admin_bp.route("/treks", methods=["GET"])
@role_required("Admin")
def get_treks():

    #treks = Trek.query.order_by(Trek.id.desc()).limit(5).all()
    treks = Trek.query.order_by(Trek.id.desc()).all()

    result = []

    for t in treks:
        result.append({
            "id": t.id,
            "name": t.name,
            "location": t.location,
            "difficulty": t.difficulty,
            "duration": t.duration,
            "slots": t.available_slots,
            "status": t.status,

            # NEW
            "assigned_staff_id" : t.assigned_staff_id,

            # NEW
            "assigned_staff_name" : t.staff.name if t.staff else None
        })

    return jsonify(result)

@admin_bp.route("/recent-treks", methods=["GET"])
@role_required("Admin")
@cache.cached(timeout=300)
def get_recent_treks():

    treks = Trek.query.order_by(Trek.id.desc()).limit(5).all()
    
    result = []

    for t in treks:
        result.append({
            "id": t.id,
            "name": t.name,
            "location": t.location,
            "difficulty": t.difficulty,
            "duration": t.duration,
            "slots": t.available_slots,
            "status": t.status,

            # NEW
            "assigned_staff_id" : t.assigned_staff_id,

            # NEW
            "assigned_staff_name" : t.staff.name if t.staff else None
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

    invalidate_trek_cache()

    return jsonify({"message": "Trek updated successfully"})

@admin_bp.route("/treks/<int:trek_id>", methods=["DELETE"])
@role_required("Admin")
def delete_trek(trek_id):

    trek = Trek.query.get_or_404(trek_id)

    db.session.delete(trek)
    db.session.commit()

    invalidate_trek_cache()

    return jsonify({"message": "Trek deleted successfully"})


# Staff Management routes==================================================================================================
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
            "phone": s.phone,
            "is_active": s.is_active
        })

    return jsonify(result)

@admin_bp.route("/staff/<int:staff_id>/status", methods=["PUT"])
@role_required("Admin")
def update_staff_status(staff_id):                              # Activate / Deactivate Staff

    data = request.get_json()

    staff = User.query.get_or_404(staff_id)

    if staff.role.name != "Trek Staff":
        return jsonify({
            "message": "User is not trek staff."
        }), 400

    if "is_active" not in data:
        return jsonify({
            "message": "is_active is required."
        }), 400

    staff.is_active = data["is_active"]

    db.session.commit()

    return jsonify({
        "message": (
            "Staff activated successfully."
            if staff.is_active
            else "Staff deactivated successfully."
        )
    })


@admin_bp.route("/staff/<int:staff_id>/treks", methods=["GET"])
@role_required("Admin")
def get_staff_treks(staff_id):                                  # Get All Treks Assigned To A Staff Member

    staff = User.query.get_or_404(staff_id)

    if staff.role.name != "Trek Staff":
        return jsonify({
            "message": "User is not trek staff."
        }), 400

    treks = Trek.query.filter_by(
        assigned_staff_id=staff.id
    ).order_by(Trek.start_date.desc()).all()

    result = []

    for trek in treks:

        result.append({

            "id": trek.id,

            "name": trek.name,

            "location": trek.location,

            "start_date": (
                trek.start_date.isoformat()
                if trek.start_date else None
            ),

            "end_date": (
                trek.end_date.isoformat()
                if trek.end_date else None
            ),

            "status": trek.status

        })

    return jsonify(result)

# User Management routes===================================================================================================
@admin_bp.route("/users", methods=["GET"])
@role_required("Admin")
def get_users():                                                # Get All Users

    search = request.args.get("search", "").strip()
    role = request.args.get("role", "").strip()
    status = request.args.get("status", "").strip().lower()

    query = (
        User.query
        .join(Role)
        .order_by(User.created_at.desc())
    )

    if search:
        query = query.filter(
            
            or_(
                User.name.ilike(f"%{search}%"),
                User.email.ilike(f"%{search}%")
            )
        )

    if role:
        query = query.filter(Role.name == role)

    if status == "active":
        query = query.filter(User.is_active.is_(True))

    elif status == "inactive":
        query = query.filter(User.is_active.is_(False))

    users = query.all()

    result = []

    for user in users:

        result.append({
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "phone": user.phone,
            "role": user.role.name,
            "is_active": user.is_active,
            "created_at": user.created_at.strftime("%Y-%m-%d")
        })

    return jsonify(result)


@admin_bp.route("/users/<int:user_id>/status", methods=["PUT"])
@role_required("Admin")
def update_user_status(user_id):                                # Activate / Deactivate User

    current_admin = User.query.get(int(get_jwt_identity()))

    user = User.query.get_or_404(user_id)

    if user.role.name == "Admin":
        return jsonify({
            "message": "Admin accounts cannot be modified."
        }), 400

    if current_admin.id == user.id:
        return jsonify({
            "message": "You cannot deactivate your own account."
        }), 400

    data = request.get_json()

    if "is_active" not in data:
        return jsonify({
            "message": "is_active is required."
        }), 400

    user.is_active = data["is_active"]

    db.session.commit()

    return jsonify({
        "message":
            "User activated successfully."
            if user.is_active
            else "User deactivated successfully."
    })


# Dashboard routes=========================================================================================================
@admin_bp.route("/dashboard-summary", methods=["GET"])
@role_required("Admin")
@cache.cached(timeout=300)
def dashboard_summary():

    staff_role = Role.query.filter_by(name="Trek Staff").first()

    return jsonify({
        "total_treks": Trek.query.count(),
        "total_users": User.query.count(),
        "total_staff": User.query.filter_by(role_id=staff_role.id).count(),
        "total_bookings": Booking.query.count()
    })

@admin_bp.route("/recent-bookings", methods=["GET"])
@role_required("Admin")
@cache.cached(timeout=300)
def recent_bookings():

    bookings = (
        Booking.query
        .order_by(Booking.booking_date.desc())
        .limit(5)
        .all()
    )

    result = []

    for booking in bookings:
        result.append({
            "id": booking.id,
            "user": booking.user.name,
            "trek": booking.trek.name,
            "status": booking.status,
            "booking_date": booking.booking_date.strftime("%Y-%m-%d")
        })

    return jsonify(result)



# Reports & Statistics ====================================================================================================
@admin_bp.route("/reports", methods=["GET"])
@role_required("Admin")
@cache.cached(timeout=300)
def reports():

    staff_role = Role.query.filter_by(name="Trek Staff").first()
    trekker_role = Role.query.filter_by(name="Trekker").first()

    overview = {

        "total_treks": Trek.query.count(),

        "total_bookings": Booking.query.count(),

        "total_users": User.query.count(),

        "total_staff": (
            User.query.filter_by(role_id=staff_role.id).count()
            if staff_role else 0
        ),

        "total_trekkers": (
            User.query.filter_by(role_id=trekker_role.id).count()
            if trekker_role else 0
        ),

        "open_treks":
            Trek.query.filter_by(status="Open").count(),

        "completed_treks":
            Trek.query.filter_by(status="Completed").count()

    }

    difficulty_stats = []

    difficulty_rows = (

        db.session.query(

            Trek.difficulty,

            func.count(Trek.id)

        )

        .group_by(Trek.difficulty)

        .all()

    )

    for difficulty, count in difficulty_rows:

        difficulty_stats.append({

            "difficulty": difficulty or "Unknown",

            "count": count

        })

    status_stats = []

    status_rows = (

        db.session.query(

            Trek.status,

            func.count(Trek.id)

        )

        .group_by(Trek.status)

        .all()

    )

    for status, count in status_rows:

        status_stats.append({

            "status": status,

            "count": count

        })

    top_treks = []

    popular = (

        db.session.query(

            Trek.name,

            func.count(Booking.id).label("bookings")

        )

        .outerjoin(Booking)

        .group_by(Trek.id)

        .order_by(func.count(Booking.id).desc())

        .limit(5)

        .all()

    )

    for name, bookings in popular:

        top_treks.append({

            "name": name,

            "bookings": bookings

        })

    users_by_role = []

    role_rows = (

        db.session.query(

            Role.name,

            func.count(User.id)

        )

        .join(User)

        .group_by(Role.name)

        .all()

    )

    for role, count in role_rows:

        users_by_role.append({

            "role": role,

            "count": count

        })

    current_year = datetime.utcnow().year

    monthly_bookings = []

    for month in range(1, 13):

        count = (

            Booking.query.filter(

                func.extract("year", Booking.booking_date) == current_year,

                func.extract("month", Booking.booking_date) == month

            ).count()

        )

        monthly_bookings.append({

            "month": datetime(
                current_year,
                month,
                1
            ).strftime("%b"),

            "count": count

        })

    return jsonify({

        "overview": overview,

        "difficulty_stats": difficulty_stats,

        "status_stats": status_stats,

        "top_treks": top_treks,

        "users_by_role": users_by_role,

        "monthly_bookings": monthly_bookings

    })
















