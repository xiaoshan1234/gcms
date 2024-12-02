from django.contrib import admin
from django.urls import re_path,include
from .views import fd_collect


urlpatterns = [
    re_path(r'^data_collect/?', fd_collect),
]