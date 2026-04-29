run-app:
	cd djangotutorial && python3 manage.py runserver

run-migration:
	cd djangotutorial && python3 manage.py migrate

polls-migration:
	cd djangotutorial && python3 manage.py makemigrations polls 