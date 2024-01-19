#!/bin/bash
set -e

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Build static files
python manage.py collectstatic --noinput

# Start the server
python manage.py runserver 0.0.0.0:$PORT
