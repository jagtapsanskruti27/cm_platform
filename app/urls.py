from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('register/', register_view),
    path('login/', login_view),
    path('profile/', profile_view),
    path('logout/', logout_view),
]