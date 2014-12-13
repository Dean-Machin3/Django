#URL CONF FILE
from django.conf.urls import patterns, url

#import the views for polls
from polls import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)
