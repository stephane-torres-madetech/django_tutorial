run-app:
	cd djangotutorial && python3 manage.py runserver

run-rabbitmq:
# this needs to be a version under 4.3 to work with celery,
#  there are deprecated breaking changes using a newer version of rabbitmq,
#  it would be interesting to see what the difference is using redis or sqs as a queue broker.
	docker run -d -p 5672:5672 rabbitmq:3.13

run-celery-beat:
	cd djangotutorial && celery -A mysite worker -B --loglevel=info       

run-celery-worker:
	cd djangotutorial && celery -A mysite worker --loglevel=info -P solo

run-migration:
	cd djangotutorial && python3 manage.py migrate

polls-migration:
	cd djangotutorial && python3 manage.py makemigrations polls 