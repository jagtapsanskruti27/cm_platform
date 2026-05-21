from django.urls import path
from . import views

urlpatterns = [

    path('report/<int:id>/', views.report_post),

    path('block/<int:id>/', views.block_user),

    path('search/', views.search_user),

    path('admin-page/', views.admin_page),

]