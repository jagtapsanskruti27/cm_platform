from django.urls import path
from . import views


urlpatterns = [

    path(
        "story/create/",
        views.create_story,
        name="create_story"
    ),

    path(
        "story/",
        views.story_list,
        name="story_list"
    ),

    path(
        "story/<int:story_id>/",
        views.view_story,
        name="view_story"
    ),

]