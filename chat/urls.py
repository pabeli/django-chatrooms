
from django.urls import path

from . import views

urlpatterns = [
    # Route path
    path('', views.index, name='index'),
    # Chatroom path
    path('<str:room_name>/', views.room, name='room'),
]