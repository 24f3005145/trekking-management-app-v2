# Standard Library ========================================================================================================
import csv
import os
from datetime import datetime

# Flask ===================================================================================================================
from flask import current_app

# Application Extensions ==================================================================================================
from app.extensions import db

# Models ==================================================================================================================
from app.models.booking import Booking
from app.models.export_job import ExportJob

# Celery ==================================================================================================================
from app.celery_tasks import celery

# Export Tasks ============================================================================================================
@celery.task(bind=True)
def export_booking_history(self, export_job_id):

    job = ExportJob.query.get(export_job_id)

    if not job:
        return

    try:

        job.status = "Processing"
        db.session.commit()

        # ---------------------------------------------------------
        # Create export directory if it does not exist.
        # ---------------------------------------------------------

        os.makedirs(
            current_app.config["EXPORT_FOLDER"],
            exist_ok=True
        )

        filename = (
            f"bookings_user_{job.user_id}_"
            f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        )

        filepath = os.path.join(
            current_app.config["EXPORT_FOLDER"],
            filename
        )

        # ---------------------------------------------------------
        # Fetch all bookings for the user.
        # ---------------------------------------------------------

        bookings = Booking.query.filter_by(
            user_id=job.user_id
        ).all()

        # ---------------------------------------------------------
        # Write CSV file.
        # ---------------------------------------------------------

        with open(
            filepath,
            "w",
            newline="",
            encoding="utf-8"
        ) as csvfile:

            writer = csv.writer(csvfile)

            writer.writerow([
                "Trek",
                "Location",
                "Difficulty",
                "Duration",
                "Booking Date",
                "Booking Status",
                "Payment Status"
            ])

            for booking in bookings:

                writer.writerow([
                    booking.trek.name,
                    booking.trek.location,
                    booking.trek.difficulty,
                    booking.trek.duration,
                    booking.booking_date.strftime("%Y-%m-%d"),
                    booking.status,
                    booking.payment_status
                ])

        # ---------------------------------------------------------
        # Update export job.
        # ---------------------------------------------------------

        job.filename = filename
        job.status = "Completed"
        job.completed_at = datetime.utcnow()

        db.session.commit()

        return filename

    except Exception:

        job.status = "Failed"
        db.session.commit()

        raise
