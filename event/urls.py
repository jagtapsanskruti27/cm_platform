from django.urls import path
from . import views

urlpatterns = [

    # primary events page
    path('events/', views.event_page, name='events'),

    # alternative paths used elsewhere (support both /event and /feed/event)
    path('event/', views.event_page, name='event'),
    path('feed/event/', views.event_page, name='feed_event'),

    path(
        'join-event/<int:event_id>/',
        views.join_event,
        name='join_event'
    ),

    path(
        'notifications/',
        views.notifications_page,
        name='notifications'
    ),

    path('delete-event/<int:event_id>/', views.delete_event, name='delete_event'),
    
]