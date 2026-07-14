from flask import Flask
from app.config import Config
from app.extensions import db, migrate, jwt, cache, mail
from app import models
from app.celery_app import make_celery
from flask_cors import CORS

from app.routes.auth import auth_bp
from app.routes.dashboard import dashboard_bp
from app.routes.admin import admin_bp
from app.routes.user import user_bp
from app.routes.staff import staff_bp
from app.routes.mail import mail_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # CORS Configuration
    CORS(app, resources={r"/api/*": {"origins": "http://localhost:5173"}})

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    # Initialize Redis cache
    cache.init_app(app)

    # Initialize Mail 
    mail.init_app(app)

    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(dashboard_bp, url_prefix="/api")
    app.register_blueprint(admin_bp, url_prefix="/api/admin")
    app.register_blueprint(user_bp, url_prefix="/api/user")
    app.register_blueprint(staff_bp, url_prefix="/api/staff")
    app.register_blueprint(mail_bp, url_prefix="/api/mail")

    app.celery = make_celery(app)

    with app.app_context():
        db.create_all()

    return app