from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('<int:shoe_id>', views.view_reviews, name="view_reviews"),
]
