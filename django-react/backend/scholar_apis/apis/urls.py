from django.urls import path

from . import views

urlpatterns = [
    path('author/all', views.AllAuthors),
    path('author/id=<int:ID>/', views.AuthorById),
]
