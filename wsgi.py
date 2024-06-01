"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

application = get_wsgi_application()
<<<<<<< HEAD:mysite/wsgi.py
=======

>>>>>>> 2d0e7ef83622ddb9b732eb243308745fc73fc813:mysite/mysite/wsgi.py
app = application