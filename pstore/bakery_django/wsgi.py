"""
WSGI config for bakery_django project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

# Add your project directory to the sys.path
path = '/home/nongnarok20123/bakery-django/pstore'
if path not in sys.path:
    sys.path.insert(0, path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bakery_django.settings')

application = get_wsgi_application()
