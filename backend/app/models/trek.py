from app.extensions import db


class Trek(db.Model):
    __tablename__ = "treks"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(150), nullable=False)
    location = db.Column(db.String(150), nullable=False)
    difficulty = db.Column(db.String(30))
    duration = db.Column(db.Integer)

    available_slots = db.Column(
        db.Integer,
        default=0
    )

    status = db.Column(
        db.String(30),
        default="Pending"
    )

    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)

    assigned_staff_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id")
    )

    bookings = db.relationship(
    "Booking",
    back_populates="trek",
    lazy=True,
    cascade="all, delete-orphan"
    )
