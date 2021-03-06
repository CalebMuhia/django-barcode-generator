import os

from project.settings import *


DEBUG = True
TEMPLATE_DEBUG = DEBUG


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(SITE_ROOT, 'development.db'),
    }
}


SECRET_KEY = ''


WSGI_APPLICATION = 'project.wsgi.development.application'
