from django.urls import re_path
from . import consumers

websocket_urlpatterns = [

    # General Chat
    re_path(
        r"ws/general/$",
        consumers.GeneralChatConsumer.as_asgi(),
    ),

    # Private Chat
    re_path(
        r"ws/private/(?P<room>[\w-]+)/$",
        consumers.PrivateChatConsumer.as_asgi(),
    ),

]