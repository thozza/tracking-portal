from django.conf.urls import patterns, url

from tracker.views import HomeView
from tracker.views import NodeListView, NodeDetailView, NodeCreateView, NodeDeleteView
from tracker.views import SensorRecordsView
from tracker.views import RecordDeleteView

urlpatterns = patterns('',
                       url(r'^$', HomeView.as_view(), name='home'),
                       url(r'^node/$', NodeListView.as_view(), name='node_list'),
                       url(r'^node/add/$', NodeCreateView.as_view(), name='node_add'),
                       url(r'^node/(?P<pk>\d+)/$', NodeDetailView.as_view(), name='node_detail'),
                       url(r'^node/(?P<pk>\d+)/delete/$', NodeDeleteView.as_view(), name='node_delete'),
                       url(r'^record/(?P<pk>\d+)/delete/$', RecordDeleteView.as_view(), name='record_delete'),
                       url(r'^sensor/(?P<sensor_pk>\d+)/records$', SensorRecordsView.as_view(), name='sensor_records'),
                       )