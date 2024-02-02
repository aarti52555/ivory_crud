here are the steps for the projects:

step 
1. created the directory for the project
2. go to that directory using cd director_name
3. virtual env
4. cookiecutter project clone
5. install requirements using pip install -r requirements/base.txt
6. integrate the database settings.
7. run the initial migrate command
8. used cities-light Django package for the city country.

Steps for the city light:

1. pip install django-cities-light
2. add the cities-light into the installed app
3. python manage.py migrate
4. python manage.py cities_light
