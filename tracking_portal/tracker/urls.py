# -*- coding: utf-8 -*-
#
# Tracking portal for sensor data
# Copyright (C) 2014 Tomas Hozza <thozza@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# he Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
# Authors: Tomas Hozza <thozza@gmail.com>

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