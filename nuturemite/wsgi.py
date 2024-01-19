"""
WSGI config for nuturemite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

<<<<<<< HEAD
setttings_module = 'nuturemite.deployment' if 'WEBSITE_HOSTNAME' in os.environ else 'nuturemite.setttings'

os.environ.setdefault('DJANGO_SETTINGS_MODULE', setttings_module)
=======
settings_module = 'nuturemite.deployment' if 'WEBSITE_HOSTNAME' in os.environ else 'nuturemite.settings'

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nuturemite.settings')
>>>>>>> fa76898c7c21cb532ee1ad4e07e1a675ef07fc78

application = get_wsgi_application()

app = application
