import os

BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

class Config:
    SECRET_KEY = "super-secret-key"
    JWT_SECRET_KEY = "change-this-to-a-long-secret-key"
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, "instance", "tma.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # -----------------------------
    # Redis Cache Configuration
    # -----------------------------
    CACHE_TYPE = "RedisCache"
    CACHE_REDIS_HOST = "localhost"
    CACHE_REDIS_PORT = 6379
    CACHE_REDIS_DB = 0
    CACHE_DEFAULT_TIMEOUT = 300

    #----------------------Exports
    EXPORT_FOLDER = os.path.join(BASE_DIR, "exports")

    # -----------------------------
    # Mail Configuration
    # -----------------------------
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False

    MAIL_USERNAME = "classysassy2105@gmail.com"
    MAIL_PASSWORD = "tuij okgw suqy nlvf"

    MAIL_DEFAULT_SENDER = "classysassy2105@gmail.com"