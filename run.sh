#!/bin/bash

gunicorn -b 0.0.0.0:8000 -w 3 wsgi:app
