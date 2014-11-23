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
# Authors: Tomas Hozza <thozza@redhat.com>

from django.http.response import HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, TemplateView, DetailView

from tracker.models import SensorType, Sensor, Node, Record


class NodeListView(ListView):
    """
    View listing all nodes
    """
    model = Node

    def get_context_data(self, **kwargs):
        context = super(NodeListView, self).get_context_data(**kwargs)
        return context


class NodeDetailView(DetailView):
    """
    View with details about a particular Node
    """
    model = Node

    def get_context_data(self, **kwargs):
        context = super(NodeDetailView, self).get_context_data(**kwargs)
        return context


class NodeCreateView(CreateView):
    """
    View for adding Node
    """
    model = Node
    template_name_suffix = '_create'
    fields = ['address', 'firmware_name', 'firmware_version']

    def get_success_url(self):
        return reverse_lazy('tracker:node_detail', kwargs={'pk': self.object.pk})


class NodeDeleteView(DeleteView):
    """
    View for deleting a node
    """
    model = Node
    success_url = reverse_lazy('tracker:node_list')


class RecordDeleteView(DeleteView):
    """
    View for deleting a Record
    """
    model = Record
    success_url = reverse_lazy('tracker:sensor_records')


class SensorRecordsView(TemplateView):
    """
    View listing all Records for a particular Sensor
    """
    template_name = 'tracker/sensor_records.html'

    def get_context_data(self, **kwargs):
        sensor_pk = kwargs['sensor_pk']
        context = super(SensorRecordsView, self).get_context_data(**kwargs)

        context['sensor'] = sensor = Sensor.objects.get(pk=sensor_pk)
        context['record_list'] = sensor.record_set.all()
        return context


class HomeView(TemplateView):
    template_name = 'tracker/home.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(HomeView, self).get_context_data(**kwargs)
        return context

