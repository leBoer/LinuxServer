#!/usr/bin/python
import sys
import logging
from catalog import app as application

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, "/var/www/app/app")

application.secret_key = 'supersecretkey'
