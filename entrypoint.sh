#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for PostgreSQL..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
        sleep 0.1
    done

    echo "PostgreSQL started."
    echo "-------------------"
    echo ""
fi

if [ "$FLASK_ENV" = "development" ]
then
    echo "Creating the database tables..."
    python manage.py create_db
    echo "Tables created"
    echo "-------------------"
    echo ""

    
fi

echo "Performing any database migrations..."
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
echo "Migrations completed successfully"
echo "-------------------"
echo ""

exec "$@"