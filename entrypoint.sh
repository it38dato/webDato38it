#!/bin/sh
set -e
echo "Waiting for database..."
#python manage.py migrate
python manage.py migrate --noinput
echo "Collecting static files..."
python manage.py collectstatic --noinput
echo "Starting Gunicorn..."
exec gunicorn dato138it.wsgi:application --bind 0.0.0.0:8000