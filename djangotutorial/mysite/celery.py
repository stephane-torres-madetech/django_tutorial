import os
from celery import Celery
from .tasks import test_task, get_questions


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

app = Celery("mysite")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()

@app.on_after_finalize.connect
def setup_periodic_tasks(sender: Celery, **kwargs):
    sender.add_periodic_task(3, test_task.s("This a test"), name="testing")
    sender.add_periodic_task(6, get_questions.s(1), name="testing getting objects from db")

