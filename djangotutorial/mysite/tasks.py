import os
import django
from celery import shared_task

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

# 2. Trigger the setup
django.setup()


from polls.models import Question

@shared_task(name="test")
def test_task(message: str):
    
    print(message)

@shared_task(name="question")
def get_questions(q_id: str):
    try:
        question = Question.objects.get(pk=q_id)
        print(question.__str__())
    except Question.DoesNotExist:
        print("Could not find question")

