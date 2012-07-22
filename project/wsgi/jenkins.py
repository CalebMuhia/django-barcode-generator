from django.core.wsgi import get_wsgi_application

import os


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings.jenkins")
application = get_wsgi_application()
