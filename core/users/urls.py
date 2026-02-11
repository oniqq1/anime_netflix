from django.contrib import admin
from django.urls import path , include
from .views import logout_view , register_view , login_view, profile_view, profile_settings


urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path("profile/", profile_view, name="profile"),
    path("settings/", profile_settings, name="settings")
    ]