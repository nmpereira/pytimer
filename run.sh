#!/bin/bash
source .venv/scripts/activate
export FLASK_APP=app.py
export FLASK_ENV=development
flask run