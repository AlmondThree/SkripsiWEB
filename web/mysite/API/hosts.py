from django.conf import settings
from . import urls
from django_hosts import patterns, host

host_patterns = patterns('',
    host(r'www', settings.ROOT_URLCONF, name='www'),
    host(r'(?!www)\w+', 'API.urls', name='wildcard'),
    host(r'api', urls, name='api')
)