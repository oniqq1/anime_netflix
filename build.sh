#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt


python core/manage.py migrate
mkdir -p logs
python core/manage.py collectstatic --noinput
