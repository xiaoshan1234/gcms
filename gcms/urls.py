"""gcms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include,re_path,path
import app_index.views as v_idx
import app_file_auth.views as v_fa

urlpatterns = [
    re_path(r'^admin/?', admin.site.urls),
    re_path(r'^index/?', v_idx.index),  
    re_path(r'^staff/?', include("app_staff_ms.urls")), 
    re_path(r'^bdms/?', include("app_bdms.urls")),  
    path('fa/<path:file_path>', v_fa.file_auth),  
    re_path('', v_idx.index)
]
