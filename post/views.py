import base64

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Post, Like, Comment
from event.models import Event, Notification


@login_required
def feed(request):
    posts = Post.objects.all().order_by('-id')
    events = Event.objects.all().order_by('event_date')[:3]
    notifications = Notification.objects.filter(user=request.user).order_by('-created_at')[:5]

    query = request.GET.get('q', '').strip()
    users = []

    if query:
        users = User.objects.filter(username__icontains=query)

    return render(request, 'feed.html', {
        'posts': posts,
        'events': events,
        'notifications': notifications,
        'users': users,
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

    Like.objects.get_or_create(
        user=request.user,
        post=post
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

    return redirect('/feed/')
