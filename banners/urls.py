from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('maintain/', views.banner_maintenance, name="banner_maintenance"),
    path('create/', views.create_banner, name="create_banner"),
    path('edit/', views.edit_banner, name="edit_banner"),
    path('delete/', views.delete_banner, name="delete_banner"),
]
