"""
WSGI config for django project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.conf import settings
from django.core.wsgi import get_wsgi_application

from web.tasks import warm_up_with_default_test_net_sender_and_gift

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

def app_with_warm_up():
    if settings.DEBUG:
        warm_up_with_default_test_net_sender_and_gift()

    return get_wsgi_application()

application = app_with_warm_up()
