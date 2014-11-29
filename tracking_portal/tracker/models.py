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

from django.db import models
from django_enumfield import enum


class Record(models.Model):
    """
    Class for a single measurement.
    """
    timestamp = models.DateTimeField()
    value = models.FloatField()
    sensor = models.ForeignKey('Sensor')

    def __unicode__(self):
        return "<Record: time={0} value={1} sensor={2}>".format(self.timestamp,
                                                                self.value,
                                                                self.sensor)

    class Meta:
        # there should be only one value fom sensor at the time
        unique_together = ('timestamp', 'sensor')
        ordering = ['timestamp']


class Node(models.Model):
    """
    Class representing a Node with multiple sensors.
    """
    address = models.PositiveIntegerField(unique=True, help_text='Node address')
    firmware_name = models.CharField(max_length=30, blank=True, help_text='Node firmware name')
    firmware_version = models.CharField(max_length=30, blank=True, help_text='Node firmware version')

    def __unicode__(self):
        return "<Node addr={0} fw={1} fw_ver={2}>".format(self.address, self.firmware_name, self.firmware_version)


class SensorType(enum.Enum):
    """
    Class representing a particular sensor type
    """
    DOOR = 0
    MOTION = 1
    SMOKE = 2
    LIGHT = 3
    DIMMER = 4
    COVER = 5
    TEMP = 6
    HUM = 7
    BARO = 8
    WIND = 9
    RAIN = 10
    UV = 11
    WEIGHT = 12
    POWER = 13
    HEATER = 14
    DISTANCE = 15
    LIGHT_LEVEL = 16
    ARDUINO_NODE = 17
    ARDUINO_REPEATER_NODE = 18
    LOCK = 19
    IR = 20
    WATER = 21
    AIR_QUALITY = 22
    CUSTOM = 23
    DUST = 24
    SCENE_CONTROLLER = 25

    labels = {
        DOOR: 'Door',
        MOTION: 'Motion',
        SMOKE: 'Smoke',
        LIGHT: 'Light',
        DIMMER: 'Dimmer',
        COVER: 'Cover',
        TEMP: 'Temperature',
        HUM: 'Humidity',
        BARO: 'Barometric Pressure',
        WIND: 'Wind Speed',
        RAIN: 'Rain',
        UV: 'UV Light',
        WEIGHT: 'Weight',
        POWER: 'Power',
        HEATER: 'Heater',
        DISTANCE: 'Distance',
        LIGHT_LEVEL: 'Light Level',
        ARDUINO_NODE: 'Arduino Node',
        ARDUINO_REPEATER_NODE: 'Arduino Repeater Node',
        LOCK: 'Lock',
        IR: 'Infrared',
        WATER: 'Water',
        AIR_QUALITY: 'Air Quality',
        CUSTOM: 'Custom',
        DUST: 'Dust',
        SCENE_CONTROLLER: 'Scene Controller'
    }


class Sensor(models.Model):
    """
    Class representing a particular sensor.
    """
    id_on_node = models.PositiveIntegerField(help_text='Sensor ID on a particular Node')
    type = enum.EnumField(SensorType, default=SensorType.TEMP, help_text='Sensor type')
    node = models.ForeignKey('Node')

    def get_type_string(self):
        return SensorType.label(self.type)

    def __unicode__(self):
        return "<Sensor id={0} type={1} node={2}>".format(self.id_on_node, self.get_type_string(), self.node)

    class Meta:
        unique_together = ('node', 'id_on_node')