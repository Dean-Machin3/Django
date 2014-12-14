#URL CONF FILE
from django.conf.urls import patterns, url

#import the views for polls
from polls import views

urlpatterns = patterns('',
    #index view loading
    #ex: polls/
    url(r'^$', views.index, name='index'),

    #other view loading with pram
    #ex: polls/
    url(r'^(?P<question_id>\d+)/$', views.detail, name='detail'),
    #ex: polls/5/results
    url(r'^(?P<question_id>\d+)/results/$', views.results, name='results'),
    #ex: polls/5/vote
    url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),

)
