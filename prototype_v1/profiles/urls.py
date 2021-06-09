from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginPage, name='login'),
    path('register/', views.register, name='register'),
    path('logout/',views.logout_view, name='logout'),
    path('profile_setup/', views.profile_setup, name='profile_setup'),
]