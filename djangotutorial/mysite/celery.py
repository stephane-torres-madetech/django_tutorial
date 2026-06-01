import os
from celery import Celery
from .tasks import test_task


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

app = Celery("mysite")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()

@app.on_after_finalize.connect
def setup_periodic_tasks(sender: Celery, **kwargs):
    sender.add_periodic_task(5, test_task.s("This a test"), name="testing")

# @app.on_after_finalize.connect
# def setup_periodic_tasks(sender: Celery, **kwargs):
#     sender.add_periodic_task(10, test_task.s("This a test"), name="testing")

# @app.task
# def test_task(message: str):
    
#     print(message)
