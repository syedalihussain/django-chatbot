from django.urls import path, re_path

from chat import views

app_name = 'chat'

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^(?P<room_name>[^/]+)/$', views.room, name='room'),
]
