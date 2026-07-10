from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', home),
    path('register/', register_view),
    path('admin-register/', views.admin_register_view, name='admin_register'),
    path('admin-approve/<str:token>/', views.admin_approve_view, name='admin_approve'),
    path('login/', login_view, name='login'),
    path("admin-login/", views.admin_login_view, name="admin_login"),
    path('profile/', profile_view),
    path('logout/', views.logout_view, name='logout'),
    path('edit-profile/', edit_profile, name='edit_profile'),
    path('follow/<int:user_id>/', follow_user, name='follow_user'),

    # path('dashboard/', dashboard, name='dashboard'),  # 👈 ADD THIS

    path(
        'forgot-password/',
        auth_views.PasswordResetView.as_view(
            template_name='forgot_password.html'
        ),
        name='password_reset'
    ),

    path(
        'forgot-password/',
        auth_views.PasswordResetView.as_view(
            template_name='forgot_password.html'
        ),
        name='password_reset'
    ),

    path(
        'forgot-password/done/',
        auth_views.PasswordResetDoneView.as_view(
            template_name='password_reset_done.html'
        ),
        name='password_reset_done'
    ),

    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='password_reset_confirm.html'
        ),
        name='password_reset_confirm'
    ),

    path(
        'reset/done/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='password_reset_complete.html'
        ),
        name='password_reset_complete'
    ),

    
]