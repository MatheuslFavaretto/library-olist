#!/bin/bash

python manage.py test

python manage.py makemigrations
python manage.py migrate

python manage.py import_authors authors.csv

nohup python manage.py runserver 0.0.0.0:8000 &

tail -f /dev/null
