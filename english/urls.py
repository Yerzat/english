from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'english.views.home', name='home'),
    # url(r'^english/', include('english.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'words.views.home', name='home'),
    url(r'^populate$', 'freq_words.views.populate', name='populate'),
    url(r'^test$', 'freq_words.views.test', name='test'),
    url(r'^populate_litvinov', 'litvinov.views.populate', name='populate_litvinov'),
    url(r'^litvinov', 'linew_litvinov.views.populate', name='litvinov'),
    url(r'^cards$', 'linew_litvinov.views.words', name='cards'),
    url(r'^card/(?P<card_id>\d+)/$', 'linew_litvinov.views.card', name='card'),
    url(r'^my_profile$', 'linew_litvinov.views.my_profile', name='my_profile'),
    url(r'^add_card/(?P<card_id>\d+)/$', 'linew_litvinov.views.add_card', name='add_card'),
    url(r'^see_card/(?P<card_id>\d+)/(?P<i>\d+)/(?P<direction>[-]?\d+)/$', 'linew_litvinov.views.see_card', name='see_card'),
    url(r'^train_card/(?P<card_id>\d+)/$', 'linew_litvinov.views.train_card', name='train_card'),
    url(r'^card_slider/(?P<card_id>\d+)/$', 'linew_litvinov.views.slider_card', name='slider_card'),
    url(r'^words/', include('words.urls')),
    url(r'^train_words/', include('train_words.urls')),
    url(r'^grammar/', include('grammar.urls')),
    url(r'^themes/$', 'linew_litvinov.views.themes', name='themes'),
    url(r'^theme_cards/(?P<theme_id>\d+)/$', 'linew_litvinov.views.theme_cards', name='theme_cards'),
)
