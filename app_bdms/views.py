from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from .views_collect import _collect_get,_collect_post
# Create your views here.

def fd_collect(req:HttpRequest):
    context = {}
    context['user'] = req.user
    if req.method == 'GET': 
        return _collect_get(req, context)
    elif req.method == 'POST':
        return _collect_post(req, context)
    

