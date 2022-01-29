from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('view/<int:shoe_id>', views.view_reviews, name="view_reviews"),
    path('write/<int:shoe_id>', views.write_review, name="write_review"),
]
