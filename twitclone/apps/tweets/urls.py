from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from tweets import views

urlpatterns = [
    url(r'^tweets/$', views.tweet_list),
    url(r'^tweets/(?P<tid>[0-9]+)$', views.tweet_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
