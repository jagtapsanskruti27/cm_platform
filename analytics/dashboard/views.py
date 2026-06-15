from django.shortcuts import render
from django.db.models import Count
from django.contrib.auth.models import User
from post.models import Post, Like


def analytics_dashboard(request):
    most_liked_posts = Post.objects.annotate(
        like_count=Count('like')
    ).order_by('-like_count', '-created_at')[:5]

    user_activity = User.objects.annotate(
        post_count=Count('post')
    ).order_by('-post_count')

    total_posts = Post.objects.count()
    total_users = User.objects.count()
    total_likes = Like.objects.count()

    return render(request, 'analytics/dashboard.html', {
        'most_liked_posts': most_liked_posts,
        'user_activity': user_activity,
        'total_posts': total_posts,
        'total_users': total_users,
        'total_likes': total_likes,
    })
