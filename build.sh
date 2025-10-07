#!/bin/bash
pip install -r requirements.txt
npm install
npm run build
cd backend
python manage.py collectstatic --noinput
python manage.py migrate
