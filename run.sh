#!/bin/bash

echo "Public IP: $(curl https://ipinfo.io/ip)"

if [[ "$ENVIRONMENT" == "DEV" ]]
then
    pipenv install --dev

    python manage.py migrate
    
    echo "yes" | python manage.py flush

    python manage.py runserver 0.0.0.0:8000
else
    pipenv install

    python manage.py migrate

    python manage.py real_seed

    /usr/local/bin/gunicorn wsgi:application --bind 0.0.0.0:8000
fi
