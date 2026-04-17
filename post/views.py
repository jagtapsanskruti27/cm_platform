import base64

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post, Like, Comment


@login_required
def feed(request):
    posts = Post.objects.all().order_by('-id')
    return render(request, 'feed.html', {'posts': posts})


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
