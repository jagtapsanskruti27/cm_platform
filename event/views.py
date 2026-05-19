from .models import Event, EventJoin, Notification
from .forms import EventForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404


@login_required
def event_page(request):

    events = Event.objects.all().order_by('-created_at')

    form = EventForm()

    if request.method == 'POST':

        form = EventForm(request.POST)

        if form.is_valid():

            event = form.save(commit=False)

            event.user = request.user

            event.save()

            return redirect('events')

    context = {
        'events': events,
        'form': form
    }

    return render(
        request,
        'event/event.html',
        context
    )


@login_required
def join_event(request, event_id):

    event = get_object_or_404(Event, id=event_id)

    already_joined = EventJoin.objects.filter(
        event=event,
        user=request.user
    ).exists()

    if not already_joined:

        EventJoin.objects.create(
            event=event,
            user=request.user
        )

    Notification.objects.create(
    user=event.user,
    event=event,
    message=f"{request.user.username} joined your event: {event.title}"
)

    return redirect('events')


@login_required
def notifications_page(request):

    notifications = Notification.objects.filter(
        user=request.user
    ).order_by('-created_at')

    return render(
        request,
        'event/notifications.html',
        {'notifications': notifications}
    )

@login_required
def delete_event(request, event_id):

    event = get_object_or_404(Event, id=event_id)

    event.delete()

    return redirect('events')