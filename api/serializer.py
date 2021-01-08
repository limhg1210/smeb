from rest_framework import serializers
from layout.models import Setting
from users.models import User, Department, Position


class SettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Setting
        fields = '__all__'


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
