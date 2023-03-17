from django.urls import path,include
from django.contrib.auth import views as authentication_views
from . import views


app_name = "users"

urlpatterns = [
   path('register/',views.register,name='register'),
   path('profile/',views.profilePage,name='profile')
]  