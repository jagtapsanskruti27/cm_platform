from django.urls import path
from . import views

urlpatterns = [

    # General Chat
    path(
        "chat/",
        views.chat_index,
        name="chat_index"
    ),

    path(
        "chat/<str:room>/",
        views.chat_page,
        name="chat"
    ),

    # Private Chat
    path(
        "chat/private/<int:user_id>/",
        views.private_chat,
        name="private_chat"
    ),

]