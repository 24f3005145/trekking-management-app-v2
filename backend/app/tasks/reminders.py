from datetime import date, timedelta

from app.celery_tasks import celery

from app.models.trek import Trek
from app.services.mail_service import MailService


@celery.task(name="app.tasks.reminders.daily_trek_reminders")
def daily_trek_reminders():

    tomorrow = date.today() + timedelta(days=1)

    treks = Trek.query.filter(

        Trek.status == "Open",

        Trek.start_date == tomorrow

    ).all()

    reminder_count = 0

    for trek in treks:

        from app.models.booking import Booking

        bookings = Booking.query.filter_by(
            trek_id=trek.id,
            status="Booked"
        ).all()

        for booking in bookings:

            user = booking.user

            try:
                MailService.send_email(

                    recipients=[user.email],

                    subject="Reminder: Your Trek Starts Tomorrow!",

                    body=f"""
                    Hello {user.name},

                    This is a reminder that your trek:

                    {trek.name}

                    starts tomorrow.

                    Location : {trek.location}
                    Difficulty : {trek.difficulty}
                    Duration : {trek.duration} day(s)

                    Please report at the designated meeting point on time.

                    Happy Trekking!

                    Trekking Management Team
                    """

                )

                reminder_count += 1
            
            except Exception as e:
                print(f"Failed to send reminder to {user.email}: {e}")

        print(f"Daily Reminder Job Completed - {reminder_count} emails sent")

    return reminder_count