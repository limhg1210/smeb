from django.views.generic import View
from django.shortcuts import render


class CalendarView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'schedules/calendar.html')
