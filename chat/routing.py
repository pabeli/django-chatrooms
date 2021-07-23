from django.urls import re_path
"""
Sometimes a regular path doesn't quite meet
our requirements for our piece of software
"""

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)', consumers.ChatRoomConsumer)
]