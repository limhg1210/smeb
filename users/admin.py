from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, Department, Position


class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'name', 'nickname', 'department', 'position')

    UserAdmin.fieldsets[1][1]['fields'] = (
        'name', 'nickname', 'department', 'position', 'duty',
        'phone', 'email', 'join_date', 'leave_date', 'photo',
        'author', 'status',
    )

    UserAdmin.add_fieldsets += (
        ('추가정보', {'fields': (
            'name', 'nickname', 'department', 'position', 'duty',
            'phone', 'email', 'join_date', 'leave_date', 'photo',
            'author', 'status',
        )}),
    )


admin.site.register(User, CustomUserAdmin)
admin.site.register(Department)
admin.site.register(Position)
