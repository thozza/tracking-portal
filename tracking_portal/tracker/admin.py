from django.contrib import admin
from tracker.models import Meter, MeterType, MeasurementObject, Record

# registering tracker models into admin
for model in (Meter, MeterType, MeasurementObject, Record):
    admin.site.register(model)
