from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    # Examples:
    url(r'^(?P<index>\d+)/$', 'grammar.views.grammar', name='grammar'),
)