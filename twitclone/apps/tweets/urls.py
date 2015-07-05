from django.conf.urls import patterns, url

urlpatterns = patterns(
    'tweets.views',
    # api
    url(r'^api/tweets/$', 'tweet_list'),
    url(r'^api/tweets/(?P<pk>[0-9]+)$', 'tweet_detail')
)
