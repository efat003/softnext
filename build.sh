#!/bin/bash
set -o errexit

pip install --upgrade pip
pip install -r requirements.txt

# Frontend build (যদি থাকে)
if [ -f "package.json" ]; then
    npm install
    npm run build
fi

cd backend
python manage.py collectstatic --noinput
python manage.py migrate
