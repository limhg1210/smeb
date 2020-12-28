from rest_framework import generics

from layout.models import Setting
from .serializer import SettingSerializer


class SettingList(generics.CreateAPIView):
    queryset = Setting.objects.all()
    serializer_class = SettingSerializer


class SettingDetail(generics.RetrieveAPIView):
    queryset = Setting.objects.all()
    serializer_class = SettingSerializer
