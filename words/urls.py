from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'words.views.train', name='train'),
    url(r'^boot/$', 'words.views.boot', name='boot'),
)