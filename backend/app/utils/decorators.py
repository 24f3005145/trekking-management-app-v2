from functools import wraps
from flask import jsonify
from flask_jwt_extended import get_jwt, jwt_required


def role_required(role_name):
    def wrapper(fn):

        @wraps(fn)
        @jwt_required()
        def decorator(*args, **kwargs):

            claims = get_jwt()

            if claims.get("role") != role_name:
                return jsonify({
                    "message": "Access denied"
                }), 403

            return fn(*args, **kwargs)

        return decorator

    return wrapper