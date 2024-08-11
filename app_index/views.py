from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

# Create your views here.
def index(req:HttpRequest):
    context = {}
    return render(req,"app_index/index.html",context)