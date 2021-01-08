from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView
from rest_framework.generics import RetrieveAPIView, RetrieveUpdateAPIView

from layout.models import Setting
from .serializer import SettingSerializer

from users.models import User, Department, Position
from .serializer import UserSerializer, DepartmentSerializer, PositionSerializer


# [layout] Setting
class SettingList(CreateAPIView):
    queryset = Setting.objects.all()
    serializer_class = SettingSerializer


class SettingDetail(RetrieveAPIView):
    queryset = Setting.objects.all()
    serializer_class = SettingSerializer


# [users] User
class UserList(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# [users] Department
class DepartmentList(ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class DepartmentDetail(RetrieveUpdateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


# [users] Position
class PositionList(ListCreateAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer


class PositionDetail(RetrieveUpdateAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
