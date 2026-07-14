from celery import Celery
from celery.schedules import crontab

def make_celery(app):

    celery = Celery(
        app.import_name,
        broker="redis://localhost:6379/0",
        backend="redis://localhost:6379/0"
    )

    celery.conf.update(app.config)

    # Celery Beat Schedule ---------------------------------------
    celery.conf.beat_schedule = {

        "daily-trek-reminders": {

            "task": "app.tasks.reminders.daily_trek_reminders",

            # For testing
            # "schedule": 60.0,

            # Production:
            "schedule": crontab(hour=8, minute=0)

        },
        
        # Monthly Admin Activity Report ---------------------------
        "monthly-admin-report": {

            "task": "app.tasks.reports.monthly_admin_report",

            # Testing
            # "schedule": 60.0,

            # Production
            "schedule": crontab(
                day_of_month=1,
                hour=8,
                minute=0
            )

        }

    }

    # ---------------------------------------------
    # Ensures every Celery task runs inside
    # the Flask application context.
    # ---------------------------------------------

    class ContextTask(celery.Task):

        def __call__(self, *args, **kwargs):

            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask

    return celery