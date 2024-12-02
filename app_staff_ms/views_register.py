from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login,logout

from .models import Staff
from .forms import UserNameLoginForm,UserEmailLoginForm,UserRegsiterForm

# Create your views here.

def _register_post(req:HttpRequest, context:dict) -> HttpResponse:
    form_obj = UserNameLoginForm(data=req.POST)
    print(form_obj.errors)
    next_page = req.POST.get('next')
    if form_obj.is_valid():
        c_data = form_obj.cleaned_data
        auth_user = authenticate(req, username=c_data.get("username"), password=c_data.get("password") ) 
        if auth_user:
            login(req,auth_user)
            if next_page:
                return redirect(to=next_page)
            else:
                return redirect(to='/index')
        else:
            form_obj.add_error("password","密码或邮箱错误")
            context["form"] = form_obj               
    return render(req,"app_staff/login_name.html",context)

def _register_get(req:HttpRequest, context:dict) -> HttpResponse:
    # context['next'] = req.GET.get('next') #为了能够回到原始界面，传递next参数给页面
    return render(req,"app_staff/register.html",context)
          