"""
WSGI config for blogproject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# TODO 在线上环境时 Gunicorn 加载运行
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blogproject.settings.production')

application = get_wsgi_application()
