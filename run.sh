#!/bin/bash

if [[ $1 == "dev" ]]; then
    echo "Running on Development mode!"
    hug -f app.py
elif [[ $1 == "prod" ]]; then
    echo "Running on Production mode."
    gunicorn --bind 0.0.0.0:8000 app:__hug_wsgi__
fi

echo "Run with 'dev' or 'prod'."
