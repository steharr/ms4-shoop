from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('maintain/', views.banner_maintenance, name="banner_maintenance"),
    path('create/', views.create_banner, name="create_banner"),
    path('edit/<int:banner_id>', views.create_banner, name="create_banner"),
    path('delete/<int:banner_id>', views.delete_banner, name="delete_banner"),
]
