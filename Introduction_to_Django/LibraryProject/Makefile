#make server -  to start/update the server
server:
	python manage.py runserver

#make db - to implement changes in models to database
db:
	python manage.py makemigrations
	python manage.py migrate

#make db server - to do but update db and run server
all:
	python manage.py makemigrations
	python manage.py migrate
	python manage.py runserver

#make app  - to start an app. app_name parameter is required
app:
	python manage.py startapp
