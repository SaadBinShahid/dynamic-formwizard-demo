from django.conf.urls import patterns
from django.conf.urls import url


urlpatterns = patterns('demo.views',
    url(r'^/?$', 'contact_wizard', name='contact_wizard'),
    url(r'^done/?$', 'done', name='done'),
)
