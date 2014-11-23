from django.conf.urls import patterns, url

from tracker.views import HomeView
from tracker.views import NodeListView, NodeDetailView, NodeCreateView, NodeDeleteView

urlpatterns = patterns('',
                       url(r'^$', HomeView.as_view(), name='home'),
                       url(r'^node/$', NodeListView.as_view(), name='node_list'),
                       url(r'^node/add/$', NodeCreateView.as_view(), name='node_add'),
                       url(r'^node/(?P<pk>\d+)/$', NodeDetailView.as_view(), name='node_detail'),
                       url(r'^node/(?P<pk>\d+)/delete/$', NodeDeleteView.as_view(), name='node_delete'),
                       )