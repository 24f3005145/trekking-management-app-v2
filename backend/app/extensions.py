from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()


from flask_caching import Cache

# Redis cache
cache = Cache()


from flask_mail import Mail

# Mail
mail = Mail()