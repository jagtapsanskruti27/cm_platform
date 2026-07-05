from django.urls import path
from . import views

# from .views import admin_dashboard

urlpatterns = [
    path("dashboard/", views.admin_dashboard, name="admin_dashboard"),
    path("users/", views.admin_users, name="admin_users"),
    path("posts/", views.admin_posts, name="admin_posts"),
    path("comments/", views.admin_comments, name="admin_comments"),
    path("events/", views.admin_events, name="admin_events"),
    path("reports/", views.admin_reports, name="admin_reports"),
    path("blocked-users/", views.admin_blocked_users, name="admin_blocked_users"),
]