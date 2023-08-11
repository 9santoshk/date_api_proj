#!/bin/sh
export FLASK_APP=./dateapi/run.py
pipenv run flask --debug run -h 0.0.0.0