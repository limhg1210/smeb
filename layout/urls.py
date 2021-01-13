from django.urls import path

from . import views

app_name = 'layout'

urlpatterns = [
    path('', views.LayoutView.as_view(), name='layout'),
    path('snpt_dragndrop', views.snpt_dragndrop, name='snpt_dragndrop'),
]
