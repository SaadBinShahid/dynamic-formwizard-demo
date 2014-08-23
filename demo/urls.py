from django.conf.urls import patterns
from django.conf.urls import url


urlpatterns = patterns('demo.views',
    url(r'^/?$', 'home', name='home'),
    url(r'^(?P<step>[^/]+)/?$', 'contact_wizard', name='contact_wizard'),
)
