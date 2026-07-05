from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import Message, UserStatus


# ======================================
# GENERAL CHAT
# ======================================

@login_required
def chat_index(request):
    return redirect("chat", room="general")


@login_required
def chat_page(request, room):

    messages = Message.objects.filter(
        group_name=room
    ).order_by("created_at")

    is_online = False
    last_seen = None

    try:
        status = UserStatus.objects.get(user=request.user)
        is_online = status.is_online
        last_seen = status.last_seen
    except UserStatus.DoesNotExist:
        pass

    return render(
        request,
        "chat/chat.html",
        {
            "room": room,
            "messages": messages,
            "is_online": is_online,
            "last_seen": last_seen,
        }
    )


# ======================================
# PRIVATE CHAT
# ======================================

@login_required
def private_chat(request, user_id):

    other_user = User.objects.get(id=user_id)

    ids = sorted([
        request.user.id,
        other_user.id
    ])

    room = f"private_{ids[0]}_{ids[1]}"

    messages = Message.objects.filter(
        group_name=room
    ).order_by("created_at")

    is_online = False
    last_seen = None

    try:
        status = UserStatus.objects.get(user=other_user)
        is_online = status.is_online
        last_seen = status.last_seen
    except UserStatus.DoesNotExist:
        pass

    return render(
        request,
        "chat/private_chat.html",
        {
            "room": room,
            "messages": messages,
            "other_user": other_user,
            "is_online": is_online,
            "last_seen": last_seen,
        }
    )
