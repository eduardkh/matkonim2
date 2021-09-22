#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "+++++++++++++++++++++++"
    echo "Waiting for postgres..."
    echo "+++++++++++++++++++++++"

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "+++++++++++++++++++++++"
    echo "PostgreSQL started"
    echo "+++++++++++++++++++++++"
fi

# python manage.py flush --no-input
# python manage.py migrate

exec "$@"