#!/bin/sh
# todo: for debug

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

python manage.py makemigrations
python manage.py migrate
# python manage.py collectstatic --no-input --clear

if [ "$DEBUG" = "1" ]
then
    echo "Create debug user..."

    echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin')" | python manage.py shell

fi

exec "$@"
