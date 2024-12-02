from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.core.files import File
from .forms import *
# Create your views here.

def _collect_get(req:HttpRequest, context:dict) -> HttpResponse:
    context['next'] = req.GET.get('next') # 为了能够回到原始界面，传递next参数给页面
    return render(req,"app_bdms/data_collect.html",context)


def _collect_post(req:HttpRequest, context:dict) -> HttpResponse:
    post_data = req.POST.copy()
    post_data['owner'] = req.user
    form_obj = DataCollectForm(data=post_data,files=req.FILES)
    print(form_obj.errors)
    next_page = req.POST.get('next')
    if form_obj.is_valid():
        form_obj.save()       
        return HttpResponse("success")
    else:
        context["form"] = form_obj 
        return render(req,"app_bdms/data_collect.html",context)
    
    
