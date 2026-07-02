from app import create_app

app = create_app()
celery = app.celery


@celery.task
def test_task():
    print("Celery is working!")
    return "success"