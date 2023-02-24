#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt
mkdir -p media/profile-photo
python manage.py collectstatic --no-input
python manage.py migrate