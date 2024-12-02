from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from .views_login import _login_get, _login_post
from .views_register import _register_get, _register_post
# Create your views here.

def login(req:HttpRequest):
    context = {}
    context['user'] = req.user
    if req.method == 'GET': 
        return _login_get(req, context)
    elif req.method == 'POST':
        return _login_post(req, context)

def register(req:HttpRequest):
    context = {}
    if req.method == 'GET': 
        return _register_get(req, context)