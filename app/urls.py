from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('register/', register_view),
    path('login/', login_view),
    path('profile/', profile_view),
    path('logout/', logout_view),
    path('edit-profile/', edit_profile, name='edit_profile'),
    path('follow/<int:user_id>/', follow_user, name='follow_user'),
]