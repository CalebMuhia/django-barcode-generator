import os

from project.settings import *


DEBUG = False
TEMPLATE_DEBUG = DEBUG


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(SITE_ROOT, 'development.db'),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}


SECRET_KEY = ''


WSGI_APPLICATION = 'project.wsgi.production.application'
