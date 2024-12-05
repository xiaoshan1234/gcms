from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from urllib.parse import quote
from gcms.settings import MainLogger
from pathlib import Path

# Create your views here.

@login_required
def file_auth(request, file_path):
    #生成重定向 URL，假设你已经配置了 NGINX 来处理这个路径
    redirect_url = f"/protected_file/{quote(file_path)}"
    MainLogger.debug(redirect_url)
    response = HttpResponse()
    response['Content-Type'] = 'application/octet-stream'  # 根据需要设置 MIME 类型
    response['X-Accel-Redirect'] = redirect_url

    # 返回重定向响应
    return response