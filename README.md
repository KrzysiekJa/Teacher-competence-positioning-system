# Teacher-competence-positioning-system


### Steps to done:
```
     docker-compose run web django-admin startproject main_app .
     echo "main_app/data/" > .gitignore
     docker-compose up
     docker exec -it container_id python manage.py makemigrations
     docker exec -it container_id python manage.py migrate
     docker exec -it container_id python manage.py createsuperuser
     docker-compose up
     (and log in http://0.0.0.0:8882/admin)
```
