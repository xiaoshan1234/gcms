from django.contrib import admin
from django.urls import re_path,include
from .views import login,register


urlpatterns = [
    re_path(r'^login/?', login),
    re_path(r'^register/?', register),
]