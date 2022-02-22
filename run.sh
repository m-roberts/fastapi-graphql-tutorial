#!/bin/bash

sudo -v

# Set up venv:
#
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt

# Create models and corresponding migrations:
#
# orator make:model User -m
# orator make:model Post -m
# orator make:model Comments -m

#######################################
# Manual step: modify migrations/*.py #
#######################################
# Users: name, address, phone number, sex
# Posts: user ID ("foreign key" based on 'id' from 'user'), title, body
# Comments: user ID ("foreign key" based on 'id' from 'user'), post ID ("foreign key" based on 'id' from 'post'), body

# Install Postgres.app, start server
# Apply the migration, run:
#
# orator migrate -c db.py

# Run tests:
#
# python3 -m pytest -s test

# Run web server:
#
uvicorn main:app --reload
