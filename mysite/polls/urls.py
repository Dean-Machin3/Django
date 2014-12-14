#URL CONF FILE
from django.conf.urls import patterns, url
#import the views for polls
from polls import views

urlpatterns = patterns('',
    #index view loading
    #ex: polls/
    url(r'^$', views.IndexView.as_view(), name='index'),

    #other view loading with pram
    #ex: polls/
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    #ex: polls/5/results
    url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
    #ex: polls/5/vote
    url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),

)
