# Create urls.py file in home dir to make apps more modularized and eliminate dependencies
from django.urls import path

from . import views

urlpatterns = [
	path('home', views.HomeView.as_view()),
	path('authorized', views.AuthorizedView.as_view()),
    path('login', views.LoginInterfaceView.as_view()),
]
