from datetime import datetime

from app.extensions import db


class ExportJob(db.Model):
    __tablename__ = "export_jobs"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    # Celery task identifier
    task_id = db.Column(
        db.String(100),
        unique=True
    )

    # Name of generated CSV file
    filename = db.Column(
        db.String(255)
    )

    # Pending | Processing | Completed | Failed
    status = db.Column(
        db.String(30),
        default="Pending"
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    completed_at = db.Column(
        db.DateTime
    )

    # Relationship with User
    user = db.relationship(
        "User",
        backref="export_jobs"
    )