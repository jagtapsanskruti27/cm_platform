from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Message, UserStatus


@login_required
def chat_index(request):
    return redirect('chat', room='general')


@login_required
def chat_page(request, room):

    messages = Message.objects.filter(
        group_name=room
    ).order_by("created_at")

    other_user = None
    is_online = False
    last_seen = None

    # for one-to-one room example: user1_user2
    if "_" in room:
        usernames = room.split("_")

        for uname in usernames:
            if uname != request.user.username:
                try:
                    other_user = User.objects.get(username=uname)
                except:
                    pass

        if other_user:
            try:
                status = UserStatus.objects.get(user=other_user)
                is_online = status.is_online
                last_seen = status.last_seen
            except:
                pass

            # mark messages as seen
            Message.objects.filter(
                sender=other_user,
                receiver=request.user,
                is_seen=False
            ).update(is_seen=True)

            messages = Message.objects.filter(
                sender__in=[request.user, other_user],
                receiver__in=[request.user, other_user]
            ).order_by("created_at")

    context = {
        "room": room,
        "messages": messages,
        "is_online": is_online,
        "last_seen": last_seen,
    }

    return render(request, "chat.html", context)