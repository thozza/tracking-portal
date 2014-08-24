from django.views.generic import ListView, TemplateView, DetailView
from tracker.models import MeterType, Record, Meter, MeasurementObject


class HomeView(TemplateView):
    template_name = 'tracker/home.html'


class MeterTypeList(ListView):
    template_name = 'tracker/meter_type/metertype_list.html'
    model = MeterType


class MeterTypeDetail(DetailView):
    template_name = 'tracker/meter_type/metertype_detail.html'
    model = MeterType

    def get_context_data(self, **kwargs):
        context = super(MeterTypeDetail, self).get_context_data(**kwargs)
        context['meters_list'] = Meter.objects.get_meters_of_type(self.kwargs['pk'])
        context['title'] = 'Meter type details'
        return context

