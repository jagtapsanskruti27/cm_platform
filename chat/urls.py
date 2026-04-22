from django.urls import path
from .views import chat_page, chat_index

urlpatterns = [
    path("chat/", chat_index, name="chat_index"),
    path("chat/<str:room>/", chat_page, name="chat"),
]