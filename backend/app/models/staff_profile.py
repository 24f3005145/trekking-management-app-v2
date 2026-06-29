from app.extensions import db


class StaffProfile(db.Model):
    __tablename__ = "staff_profiles"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        unique=True,
        nullable=False
    )

    contact_details = db.Column(db.String(200))
    status = db.Column(db.String(50), default="Active")

    user = db.relationship(
        "User",
        backref=db.backref(
            "staff_profile",
            uselist=False
        )
    )