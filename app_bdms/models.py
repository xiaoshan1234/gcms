from django.db import models
from django.contrib.auth.models import User
import gcms.settings as settings

# Create your models here.
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