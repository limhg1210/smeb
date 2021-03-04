from rest_framework import serializers
from layout.models import Setting
from users.models import User, Department, Position
from schedules.models import Schedule, Workspace, ScheduleCategory


class SettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Setting
        fields = '__all__'


# [users]
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'username', 'password', 'name', 'nickname', 'department',
            'position', 'duty', 'phone', 'email', 'join_date', 'leave_date',
            'photo', 'is_superuser', 'status',
        )
        extra_kwargs = {'password': {'write_only': True, 'required': False}}


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'


# [schedules]
class ScheduleSerializer(serializers.ModelSerializer):
    author_alias = serializers.SerializerMethodField()
    workspace_title = serializers.ReadOnlyField(source='workspace.title')
    category_name = serializers.ReadOnlyField(source='category.name')

    class Meta:
        model = Schedule
        fields = ['id', 'title', 'detail', 'started', 'ended',
                  'workspace', 'category', 'attendees', 'author',
                  'author_alias', 'workspace_title', 'category_name']

    def get_author_alias(self, obj):
        if obj.author.name:
            author_alias = obj.author.name
            if obj.author.nickname:
                author_alias = author_alias + f' {obj.author.nickname}'
            return author_alias
        else:
            return None


class WorkspaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workspace
        fields = ['id', 'title']


class ScheduleCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ScheduleCategory
        fields = ['id', 'name']
