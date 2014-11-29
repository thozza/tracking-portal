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

from rest_framework import serializers
from tracker.models import Node, Sensor, SensorType, Record


class NodeSerializer(serializers.ModelSerializer):
    """
    Serializer for Node object.
    """
    class Meta:
        model = Node
        fields = ('address', 'firmware_name', 'firmware_version')

    def validate_address(self, attrs, source):
        """
        Check that the address is a positive integer.
        :return:
        """
        value = attrs[source]
        if value < 0:
            raise serializers.ValidationError('Address can not be a negative number')
        return attrs


class SensorSerializer(serializers.ModelSerializer):
    """
    Serializer for Sensor object.
    """
    class Meta:
        model = Sensor
        fields = ('id_on_node', 'type', 'node')


class RecordSerializer(serializers.ModelSerializer):
    """
    Serializer for Record object.
    """
    class Meta:
        model = Record
        fields = ('timestamp', 'value', 'sensor')