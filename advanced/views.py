from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from post.models import Post
from .models import Report, Block
from django.contrib import messages

@login_required
def report_post(request, id):

    post = get_object_or_404(Post, id=id)

    if request.method == "POST":

        reason = request.POST.get("reason")

        Report.objects.create(
            reporter=request.user,
            post=post,
            reason=reason
        )

        messages.success(
            request,
            "Report submitted successfully."
        )

        return redirect("/feed/")

    return render(request, "report_post.html", {
        "post": post
    })

@login_required
def block_user(request, id):

    user_to_block = get_object_or_404(User, id=id)

    Block.objects.get_or_create(
        blocker=request.user,
        blocked=user_to_block
    )

    messages.success(request, "User blocked successfully.")
    return redirect("/feed/")

@login_required
def search_user(request):

    query = request.GET.get("q")

    users = []

    if query:

        users = User.objects.filter(
            username__icontains=query
        )

    return render(request, "search.html", {
        "users": users
    })

@login_required
def admin_page(request):

    if not request.user.is_staff:
        return redirect("/feed/")

    reports = Report.objects.all()

    return render(request, "admin_page.html", {
        "reports": reports
    })