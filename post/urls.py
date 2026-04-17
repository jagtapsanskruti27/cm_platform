from django.urls import path, include
from . import views 

urlpatterns = [
    path('feed/', views.feed),
    path('create-post/', views.create_post),
    path('like/<int:id>/', views.like_post),
    path('comment/<int:id>/', views.comment_post),
]