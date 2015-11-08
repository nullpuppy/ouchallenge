#!/usr/bin/env bash

apt-get update
apt-get install -y python-virtualenv python-dev postgresql-server-dev-9.3

virtualenv /vagrant/env
source /vagrant/env/bin/activate
pip install django djangorestframework psycopg2 uwsgi uwsgitop
