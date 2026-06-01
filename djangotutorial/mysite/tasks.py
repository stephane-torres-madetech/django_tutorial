from celery import shared_task

@shared_task
def test_task(message: str):
    
    print(message)