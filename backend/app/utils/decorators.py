from functools import wraps
from flask import jsonify
from flask_jwt_extended import (get_jwt, jwt_required, get_jwt_identity)

from app.models.user import User

def role_required(role_name):
    def wrapper(fn):

        @wraps(fn)
        @jwt_required()
        def decorator(*args, **kwargs):

            claims = get_jwt()

            user = User.query.get(int(get_jwt_identity()))

            if user is None:
                return jsonify({
                    "message": "User not found."
                }), 404

            if not user.is_active:
                return jsonify({
                    "message": "Your account has been deactivated."
                }), 403

            if claims.get("role") != role_name:
                return jsonify({
                    "message": "Access denied"
                }), 403

            return fn(*args, **kwargs)

        return decorator

    return wrapper