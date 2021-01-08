from django.urls import path

from . import views

app_name = 'api'

urlpatterns = [
    # layout
    path('layout/setting', views.SettingList.as_view(), name='setting_list'),
    path('layout/setting/<int:pk>', views.SettingDetail.as_view(), name='setting_detail'),

    # users
    path('users/user', views.UserList.as_view(), name='user_list'),
    path('users/user/<int:pk>', views.UserDetail.as_view(), name='user_detail'),
    path('users/department', views.DepartmentList.as_view(), name='department_list'),
    path('users/department/<int:pk>', views.DepartmentDetail.as_view(), name='department_detail'),
    path('users/position', views.PositionList.as_view(), name='position_list'),
    path('users/position/<int:pk>', views.PositionDetail.as_view(), name='position_detail'),
]
