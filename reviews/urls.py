from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('view/<int:shoe_id>', views.view_reviews, name="view_reviews"),
    path('write/<int:shoe_id>', views.write_review, name="write_review"),
    path('edit/<int:review_id>', views.edit_review, name="edit_review"),
    path('delete/<int:review_id>', views.delete_review, name="delete_review"),
]
