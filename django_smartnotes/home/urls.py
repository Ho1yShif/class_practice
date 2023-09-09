# Create urls.py file in home dir to make apps more modularized and eliminate dependencies
from django.urls import path

from . import views

urlpatterns = [
	path('', views.HomeView.as_view(), name='home'),
    path('login', views.LoginInterfaceView.as_view(), name='login'),
    path('logout', views.LogoutInterfaceView.as_view(), name='logout'),
]
