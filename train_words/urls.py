from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    # Examples:
    url(r'^(?P<card_id>\d+)/(?P<i>\d+)/$', 'train_words.views.train', name='train'),
)