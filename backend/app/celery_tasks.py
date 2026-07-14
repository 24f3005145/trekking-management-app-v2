from app import create_app

# ---------------------------------------------------------
# Create Flask application
# ---------------------------------------------------------

app = create_app()

# ---------------------------------------------------------
# Expose the configured Celery instance.
# All task modules will use this instance.
# ---------------------------------------------------------

celery = app.celery

# ---------------------------------------------------------
# Import task modules so Celery registers them.
# ---------------------------------------------------------

import app.tasks.exports
import app.tasks.reminders
import app.tasks.reports