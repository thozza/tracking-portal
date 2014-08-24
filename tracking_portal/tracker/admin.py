from django.contrib import admin
from tracker.models import Sensor, SensorType, Record, Node, MeasurementObject

# registering tracker models into admin
for model in (Sensor, SensorType, Record, Node, MeasurementObject):
    admin.site.register(model)
