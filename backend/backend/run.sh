# Run Migrations

python manage.py migrate

# Collect Static Files

python manage.py collectstatic --no-input

# Start Server

gunicorn -b 0.0.0.0:80 --workers 2 backend.wsgi
