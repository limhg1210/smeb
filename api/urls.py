from django.urls import path

from . import views

app_name = 'api'

urlpatterns = [
    path('layout/setting', views.SettingList.as_view(), name='setting_list'),
    path('layout/setting/<int:pk>', views.SettingDetail.as_view(), name='setting_detail'),
]
