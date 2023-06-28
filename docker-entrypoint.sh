#!/bin/sh

# flask db upgrade
cd o_rifas_back
exec gunicorn --bind 0.0.0.0:80 "app:create_app()"