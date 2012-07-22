from django.conf.urls import patterns, url


urlpatterns = patterns('',
    url(r'^$', 'project.core.views.home', name='home'),
)
