from django.db import models


class Record(models.Model):
    """
    Class for a single measurement.
    """
    timestamp = models.DateTimeField()
    value = models.FloatField()
    meter = models.ForeignKey('Meter')

    def __unicode__(self):
        return "{0} - {1}".format(str(self.timestamp), str(self.value))

    class Meta:
        ordering = ['timestamp']


class MeterManager(models.Manager):

    def get_meters_of_type(self, type):
        return self.filter(type__pk=type)


class Meter(models.Model):
    """
    Class representing a measuring device.
    """
    name = models.CharField(max_length=100)
    type = models.ForeignKey('MeterType')
    measurement_object = models.ForeignKey('MeasurementObject')
    objects = MeterManager()

    def __unicode__(self):
        return self.name




class MeterType(models.Model):
    """
    Class representing a type of measuring device (temperature, humidity, etc.)
    """
    name = models.CharField(max_length=100)
    unit_long = models.CharField(max_length=100, blank=True)

    def __unicode__(self):
        return "{0} ({1})".format(self.name, self.unit_long)


class MeasurementObject(models.Model):
    """
    Class representing a object (building, room, ...) where records are measured.
    """
    name = models.CharField(max_length=100)
    parent_object = models.ForeignKey('self', null=True, blank=True)

    def __unicode__(self):
        return self.name
