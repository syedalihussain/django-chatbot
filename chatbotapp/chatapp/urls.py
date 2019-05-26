from django.urls import path

from chatapp import views

app_name = 'chatapp'

urlpatterns = [
    path('bot/', views.bot, name='bot'),
    path('result/', views.result, name='result'),
]