# Standard Library ========================================================================================================
from datetime import datetime

# SQLAlchemy ==============================================================================================================
from sqlalchemy import func
 
# Celery ==================================================================================================================
from app.celery_tasks import celery

# Models ==================================================================================================================
from app.models.booking import Booking
from app.models.role import Role
from app.models.trek import Trek
from app.models.user import User

# Services ================================================================================================================
from app.services.mail_service import MailService


@celery.task(name="app.tasks.reports.monthly_admin_report")
def monthly_admin_report():

    # ---------------------------------------------------------
    # Overall Statistics
    # ---------------------------------------------------------

    total_users = User.query.count()

    total_completed_treks = Trek.query.filter_by(
        status="Completed"
    ).count()

    total_open_treks = Trek.query.filter_by(
        status="Open"
    ).count()

    total_bookings = Booking.query.count()

    confirmed_participants = Booking.query.filter_by(
        status="Booked"
    ).count()

    # ---------------------------------------------------------
    # Most Popular Treks
    # ---------------------------------------------------------

    popular_treks = (
        Booking.query
        .join(Trek)
        .with_entities(
            Trek.name,
            func.count(Booking.id).label("booking_count")
        )
        .group_by(Trek.id)
        .order_by(func.count(Booking.id).desc())
        .limit(5)
        .all()
    )

    # ---------------------------------------------------------
    # HTML Report
    # ---------------------------------------------------------

    report_date = datetime.now().strftime("%d %B %Y")

    html = f"""
    <html>
    <body style="font-family: Arial, sans-serif;">

        <h2 style="color:#198754;">
            Monthly Trek Activity Report
        </h2>

        <p>
            <strong>Report Generated:</strong> {report_date}
        </p>

        <table
            border="1"
            cellspacing="0"
            cellpadding="8"
            style="border-collapse:collapse;"
        >
            <tr>
                <th align="left">Statistic</th>
                <th align="left">Value</th>
            </tr>

            <tr>
                <td>Total Registered Users</td>
                <td>{total_users}</td>
            </tr>

            <tr>
                <td>Completed Treks</td>
                <td>{total_completed_treks}</td>
            </tr>

            <tr>
                <td>Open Treks</td>
                <td>{total_open_treks}</td>
            </tr>

            <tr>
                <td>Total Bookings</td>
                <td>{total_bookings}</td>
            </tr>

            <tr>
                <td>Confirmed Participants</td>
                <td>{confirmed_participants}</td>
            </tr>

        </table>

        <br>

        <h3>Top 5 Most Popular Treks</h3>

        <ol>
    """

    if popular_treks:

        for trek_name, booking_count in popular_treks:

            html += f"<li>{trek_name} ({booking_count} bookings)</li>"

    else:

        html += "<li>No booking data available.</li>"

    html += """

        </ol>

        <br>

        <p>
            Regards,<br>
            Trekking Management System
        </p>

    </body>
    </html>
    """

    # ---------------------------------------------------------
    # Fetch Admin Users
    # ---------------------------------------------------------

    admin_role = Role.query.filter_by(name="Admin").first()

    if not admin_role:

        print("Admin role not found.")

        return 0

    admin_users = User.query.filter_by(
        role_id=admin_role.id
    ).all()

    sent_count = 0

    for admin in admin_users:

        try:

            success = MailService.send_email(

                recipients=[admin.email],

                subject="Monthly Trek Activity Report",

                html=html

            )

            if success:
                sent_count += 1

        except Exception as e:

            print(f"Failed to send report to {admin.email}: {e}")

    print(
        f"Monthly Activity Report Completed - {sent_count} email(s) sent."
    )

    return sent_count