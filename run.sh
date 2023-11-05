#!/bin/bash

python manage.py makemigrations
python manage.py migrate

python manage.py test

python manage.py import_authors authors.csv

python manage.py runserver 0.0.0.0:8000
