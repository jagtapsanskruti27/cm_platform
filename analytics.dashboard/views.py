from django.shortcuts import render
from django.db.models import Count
from .models import Post
from django.contrib.auth.models import User

def analytics_dashboard(request):

    # Top 5 liked posts
    most_liked_posts = Post.objects.order_by('-likes')[:5]

    # User activity (number of posts per user)
    user_activity = User.objects.annotate(
        post_count=Count('post')
    )

    return render(request, 'analytics/dashboard.html', {
        'most_liked_posts': most_liked_posts,
        'user_activity': user_activity
    })