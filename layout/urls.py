from django.urls import path

from . import views

app_name = 'layout'

urlpatterns = [
    path('', views.LayoutView.as_view(), name='layout'),
    path('snippet_dragndrop', views.snippet_dragndrop, name='snippet_dragndrop'),
]
