from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView
from rest_framework.generics import RetrieveAPIView, RetrieveUpdateAPIView

from layout.models import Setting
from .serializer import SettingSerializer

from users.models import User, Department, Position
from .serializer import UserSerializer, DepartmentSerializer, PositionSerializer

from schedules.models import Schedule, Workspace, ScheduleCategory
from .serializer import ScheduleSerializer, WorkspaceSerializer, ScheduleCategorySerializer

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


# [schedules] Schedule
class ScheduleList(ListCreateAPIView):
    serializer_class = ScheduleSerializer

    def get_queryset(self):
        queryset = Schedule.objects.filter(status=True)
        queryset = queryset.select_related('author', 'workspace', 'category')
        queryset = queryset.prefetch_related('attendees')
        return queryset

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ScheduleDetail(RetrieveUpdateAPIView):
    queryset = Schedule.objects.filter(status=True)
    serializer_class = ScheduleSerializer


# [schedules] Workspace
class WorkspaceList(ListCreateAPIView):
    serializer_class = WorkspaceSerializer

    def get_queryset(self):
        queryset = Workspace.objects.filter(status=True)
        return queryset


# [schedules] ScheduleCategory
class ScheduleCategoryList(ListCreateAPIView):
    serializer_class = ScheduleCategorySerializer

    def get_queryset(self):
        queryset = ScheduleCategory.objects.filter(status=True)
        return queryset
