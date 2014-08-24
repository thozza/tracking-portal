from django.views.generic import ListView, TemplateView, DetailView
from tracker.models import SensorType, Sensor, Node, MeasurementObject, Record


class HomeView(TemplateView):
    template_name = 'tracker/home.html'

