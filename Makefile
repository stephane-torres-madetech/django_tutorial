run-app:
	cd djangotutorial && python3 manage.py runserver

run-celery:
	cd djangotutorial && celery -A mysite beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler

run-migration:
	cd djangotutorial && python3 manage.py migrate

polls-migration:
	cd djangotutorial && python3 manage.py makemigrations polls 