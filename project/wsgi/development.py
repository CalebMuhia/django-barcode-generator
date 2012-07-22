import django.core.handlers.wsgi
from django.core.wsgi import get_wsgi_application
from django.views import debug

from werkzeug.debug import DebuggedApplication
import os



os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings.development")


application = django.core.handlers.wsgi.WSGIHandler()
application = DebuggedApplication(application, evalex=True)


def null_technical_500_response(request, exc_type, exc_value, tb):
    raise exc_type, exc_value, tb

debug.technical_500_response = null_technical_500_response
