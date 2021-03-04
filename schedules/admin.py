from django.contrib import admin

from .models import Workspace, ScheduleCategory, Schedule


admin.site.register(Workspace)
admin.site.register(ScheduleCategory)
admin.site.register(Schedule)
