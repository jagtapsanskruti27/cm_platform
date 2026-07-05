from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from django.contrib.auth.models import User

from post.models import Post, Comment, Like
from event.models import Event, Notification
from app.models import Follow


@staff_member_required
def admin_dashboard(request):

    context = {

        "total_users": User.objects.count(),

        "total_posts": Post.objects.count(),

        "total_comments": Comment.objects.count(),

        "total_likes": Like.objects.count(),

        "total_events": Event.objects.count(),

        "total_notifications": Notification.objects.count(),

        "total_followers": Follow.objects.count(),

        "blocked_users": User.objects.filter(
            is_active=False
        ).count(),

        "recent_users": User.objects.order_by(
            "-date_joined"
        )[:5],

        "recent_posts": Post.objects.order_by(
            "-id"
        )[:5],

        "events": Event.objects.order_by(
            "-start_datetime"
        )[:5],
    }

    return render(
        request,
        "analytics/dashboard.html",
        context
    )


@staff_member_required
def admin_users(request):
    return render(request, "dashboard/users.html")

@staff_member_required
def admin_posts(request):
    return render(request, "dashboard/posts.html")

@staff_member_required
def admin_comments(request):
    return render(request, "dashboard/comments.html")

@staff_member_required
def admin_events(request):
    return render(request, "dashboard/events.html")

@staff_member_required
def admin_reports(request):
    return render(request, "dashboard/reports.html")

@staff_member_required
def admin_blocked_users(request):
    return render(request, "dashboard/blocked_users.html")