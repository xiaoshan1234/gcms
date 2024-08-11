from django import forms
from django.contrib.auth.models import User
from .models import *

class UserEmailLoginForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True)

class UserNameLoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True)     

# ModelForm 可以从 Model 快速创建 Form 类，避免代码重复
# ModelForm 假设你正在创建一个数据，对于已经存在的数据会添加 error
class UserRegsiterForm(forms.ModelForm):
    confirm_password = forms.CharField(required=True,max_length=20) # 正常方式构建 form
    class Meta:
        model = User # 指定 model
        fields = ["username","email","password","confirm_password"] # 选定字段      