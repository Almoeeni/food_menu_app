from django.urls import path,include
from django.contrib.auth import views as authentication_views
from . import views

urlpatterns = [
   path('register/',views.register,name='register')
]