from django.conf.urls import patterns, url

from tracker.views import HomeView, MeterTypeList, MeterTypeDetail

urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^mtype/$', MeterTypeList.as_view(), name='mtype'),
    url(r'^mtype/(?P<pk>\d+)/$', MeterTypeDetail.as_view(), name='mtype_detail'),
    url(r'^meter/$', HomeView.as_view(), name='meter'),
    url(r'^meter/(?P<meter_id>\d+)/$', HomeView.as_view(), name='meter_detail'),
    url(r'^mobject/$', HomeView.as_view(), name='mobject'),
    url(r'^mobject/(?P<mobject_id>\d+)/$', HomeView.as_view(), name='mobject_detail'),
)