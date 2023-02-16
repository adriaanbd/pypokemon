#!/bin/sh

echo "Loading postgres..."

while ! nc -z db 5432; do
  sleep 0.1
done

echo "PostgreSQL is up!"

python -m flask --app src/app.py run -h 0.0.0.0 --debug