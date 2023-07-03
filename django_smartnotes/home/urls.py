# Create urls.py file in home dir to make apps more modularized and eliminate dependencies
from django.urls import path

from . import views

urlpatterns = [
    path(home, views.home)
]
