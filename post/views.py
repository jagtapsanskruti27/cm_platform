import base64

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Post, Like, Comment, Follow
from event.models import Event, Notification
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator

@login_required
def feed(request):

    # Prevent admins from accessing the user feed
    if request.user.is_staff or request.user.is_superuser:
        return redirect("admin_dashboard")

    posts_list = Post.objects.all().order_by('-id')

    paginator = Paginator(posts_list, 5)

    page_number = request.GET.get('page')

    posts = paginator.get_page(page_number)

    events = Event.objects.all().order_by('start_datetime')[:3]

    notifications = Notification.objects.filter(
        user=request.user,
        is_read=False
    ).order_by('-created_at')

    query = request.GET.get('q', '').strip()

    users = []
    searched_posts = []

    if query:
        users = User.objects.filter(
            username__icontains=query
        )

        searched_posts = Post.objects.filter(
            caption__icontains=query
        )

    return render(request, 'feed.html', {
        'posts': posts,
        'events': events,
        'notifications': notifications,
        'users': users,
        'searched_posts': searched_posts,
        'query': query,
    })


@login_required
def create_post(request):
    if request.method == "POST":
        caption = request.POST.get('caption')
        image_file = request.FILES.get('image')

        img_base64 = ""

        if image_file:
            img_base64 = base64.b64encode(
                image_file.read()
            ).decode('utf-8')

        Post.objects.create(
            user=request.user,
            caption=caption,
            image=img_base64
        )

        return redirect('/feed/')

    return render(request, 'create_post.html')


@login_required
def like_post(request, id):
    post = Post.objects.get(id=id)

    like, created = Like.objects.get_or_create(
        user=request.user,
        post=post
    )

    if created and post.user != request.user:
        Notification.objects.create(
            user=post.user,
            message=f"{request.user.username} liked your post."
        )

    return redirect('/feed/')


@login_required
def comment_post(request, id):
    if request.method == "POST":
        post = Post.objects.get(id=id)
        text = request.POST.get('text')

        Comment.objects.create(
            user=request.user,
            post=post,
            text=text
        )

        if post.user != request.user:
            Notification.objects.create(
                user=post.user,
                message=f"{request.user.username} commented on your post."
            )

    return redirect('/feed/')


@login_required
def delete_comment(request, id):
    comment = Comment.objects.get(id=id)

    if comment.user != request.user:
        return HttpResponse("Permission Denied")

    comment.delete()

    return redirect('/feed/')



@login_required
def follow_user(request, id):
    user_to_follow = get_object_or_404(User, id=id)

    if request.user == user_to_follow:
        return HttpResponse("You cannot follow yourself")

    follow, created = Follow.objects.get_or_create(
        follower=request.user,
        following=user_to_follow
    )

    if created:
        Notification.objects.create(
            user=user_to_follow,
            message=f"{request.user.username} started following you."
        )

    return redirect('/feed/')
@login_required
def unfollow_user(request, id):
    user_to_unfollow = get_object_or_404(User, id=id)

    Follow.objects.filter(
        follower=request.user,
        following=user_to_unfollow
    ).delete()

    return redirect('/feed/')

@login_required
def delete_post(request, id):
    post = Post.objects.get(id=id)

    if post.user != request.user:
        return HttpResponse("Permission Denied")

    post.delete()

    return redirect('/feed/')

@login_required
def read_notification(request, id):
    notification = get_object_or_404(
        Notification,
        id=id,
        user=request.user
    )

    notification.is_read = True
    notification.save()

    return redirect('/feed/')


