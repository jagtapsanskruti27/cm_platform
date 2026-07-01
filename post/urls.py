from django.urls import path, include
from . import views 

urlpatterns = [
    path('feed/', views.feed),
    path('create-post/', views.create_post),
    path('like/<int:id>/', views.like_post),
    path('comment/<int:id>/', views.comment_post),
    path('delete-comment/<int:id>/', views.delete_comment),
    path('follow/<int:id>/', views.follow_user),
    path('unfollow/<int:id>/', views.unfollow_user),
    path('delete-post/<int:id>/', views.delete_post),
    path(
    'notification/read/<int:id>/',
    views.read_notification,
    name='read_notification'
),
    # path('delete-post/<int:id>/', views.delete_post),
]