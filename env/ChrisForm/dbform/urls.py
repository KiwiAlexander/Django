from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from django.contrib import admin

from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('job/', views.job, name='job'),
    path('client/', views.client, name='client'),
    path('volunteer/', views.volunteer, name='volunteer'),
]