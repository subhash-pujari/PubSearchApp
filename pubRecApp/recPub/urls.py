from django.conf.urls import patterns, url

from recPub import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'), 
    url(r'^search/$', views.search, name='search'),
    url(r'^results/(?P<pub_id>\d+)/$', views.recResult, name='recResult')
)
