from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('user-create/', views.UserCreate.as_view(), name='user_create'),
    path('user-list/', views.UserList.as_view(), name='user_list'),
    path('user-detail/<int:pk>/', views.UserDetail.as_view(), name='user_detail'),
    path('user-update/<int:pk>/', views.UserUpdate.as_view(), name='user_update'),
    path('user-delete/<int:pk>/', views.UserDelete.as_view(), name='user_delete'),
    path('change-password/<int:pk>/', views.PasswordUpdate.as_view(), name='change_password'),
]
