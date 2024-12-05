# 文件上传（分块）
## html-form 
    <input type="file" class="form-control" name="file_data" id="file_data" multiple="multiple">  
## python-model
```python
    class FieldData(models.Model):
        class Meta:
            verbose_name = settings.COMPANY_NAME+"现场数据"
            verbose_name_plural = verbose_name 
        # 如果不指定主键，会自动生成 ID主键，通过 Primary_key=True 指定主键
        owner = models.ForeignKey(to=User,on_delete=models.CASCADE) # ForeignKey ManyToManyField 
        str_data = models.CharField(max_length=200)
        # cur_time = models.DateField()
        int_data = models.IntegerField()
        file_data = models.FileField(upload_to="app_bdms/") # 这里的 url 在 django.core.files.storage.FileSystemStorage 作用下与 MEDIA_ROOT 组合
    
        def __str__(self) -> str:
            return self.owner.username  
```
## python-form
```python
class DataCollectForm(forms.ModelForm):
    class Meta:
        model = FieldData
        fields = ["owner","str_data","int_data","file_data"]
```        
## python-view
```python
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
```
# 文件下载（分块）

# 文件下载权限管理
