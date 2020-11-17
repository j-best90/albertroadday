from django.shortcuts import render
from agora.views import Agora

from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.home,name='home')
]
