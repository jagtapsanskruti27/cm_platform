import base64

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import timedelta

from .models import Story


@login_required
def create_story(request):

    if request.method == "POST":

        image = request.FILES.get("image")

        if image:

            img_base64 = base64.b64encode(
                image.read()
            ).decode("utf-8")

            Story.objects.create(
                user=request.user,
                image=img_base64
            )

        return redirect("feed")

    return render(request, "story/create_story.html")


@login_required
def story_list(request):

    stories = Story.objects.filter(
        created_at__gte=timezone.now() - timedelta(hours=24)
    ).order_by("-created_at")

    return render(
        request,
        "story/story_list.html",
        {
            "stories": stories
        }
    )


@login_required
def view_story(request, story_id):

    story = get_object_or_404(
        Story,
        id=story_id
    )

    if not story.is_active():
        story.delete()
        return redirect("feed")

    return render(
        request,
        "story/view_story.html",
        {
            "story": story
        }
    )