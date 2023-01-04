from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:title>", views.entry, name="entry"),
    path('search/', views.search, name="search"),
    path('new/', views.new, name="new"),
    path('edit/', views.edit, name="edit"),
]
