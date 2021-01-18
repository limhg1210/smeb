from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('user-create/', views.UserCreate.as_view()),
    path('user-list/', views.UserList.as_view()),
    path('user-detail/<int:pk>/', views.UserDetail.as_view()),
    path('user-update/<int:pk>/', views.UserUpdate.as_view()),
]
