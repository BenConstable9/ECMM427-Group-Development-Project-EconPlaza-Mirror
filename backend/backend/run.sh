# Run Migrations

python manage.py migrate
python manage.py createcachetable

# Collect Static Files

python manage.py collectstatic --no-input

# Create Log directories

mkdir -p /var/log/econplaza

# Start Server

gunicorn -b 0.0.0.0:80 --workers 2 --access-logfile /var/log/econplaza/gunicorn-access.log --error-logfile /var/log/econplaza/gunicorn-error.log backend.wsgi
