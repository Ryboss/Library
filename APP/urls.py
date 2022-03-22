from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('homepage',home),
    path('create_book',create_book)
]
