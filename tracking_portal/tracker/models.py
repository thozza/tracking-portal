from django.db import models


class Record(models.Model):
    """
    Class for a single measurement.
    """
    timestamp = models.DateTimeField()
    value = models.FloatField()
    sensor = models.ForeignKey('Sensor')

    def __unicode__(self):
        return "{0} - {1}".format(str(self.timestamp), str(self.value))

    class Meta:
        ordering = ['timestamp']


class MeterManager(models.Manager):

    def get_meters_of_type(self, type):
        return self.filter(type__pk=type)


class Node(models.Model):
    """
    Class representing a Node with multiple sensors.
    """
    name = models.CharField(max_length=100)
    object = models.ForeignKey('MeasurementObject')

    def __unicode__(self):
        return "<Node {0}>".format(self.name)


class SensorType(models.Model):
    """
    Class representing a particular variable that can be measured (temperature, humidity, ...)
    """
    name = models.CharField(max_length=100)
    unit_short = models.CharField(max_length=10, blank=True)
    unit_long = models.CharField(max_length=100, blank=True)

    def __unicode__(self):
        return "<SensorType {0} unit: {1}>".format(self.name, self.unit_long)


class Sensor(models.Model):
    """
    Class representing a particular sensor.
    """
    name = models.CharField(max_length=100)
    type = models.ForeignKey('SensorType')
    node = models.ForeignKey('Node')

    def __unicode__(self):
        return "<Sensor {0} of type {1} in node {2}>".format(self.name, self.type.name, self.node.name)


class MeasurementObject(models.Model):
    """
    Class representing a object (building, room, ...) where records are measured.
    """
    name = models.CharField(max_length=100)
    parent_object = models.ForeignKey('self', null=True, blank=True)

    def __unicode__(self):
        return self.name
