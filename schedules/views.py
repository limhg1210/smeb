import json

from django.views.generic import View, TemplateView
from django.shortcuts import render


class CalendarView(TemplateView):
    template_name = 'schedules/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['GET'] = json.dumps(self.request.GET, ensure_ascii=False)
        return context
