from django.db import models
from django.contrib.auth.models import User
import gcms.settings as settings
# Create your models here.
class Staff(models.Model):
    class Sex(models.IntegerChoices):
        MALE = 1
        FEMALE = 2
        SECRET = 3
    class Meta:
        verbose_name = settings.COMPANY_NAME+"员工"
        verbose_name_plural = verbose_name 
    # 如果不指定主键，会自动生成 ID主键，通过 Primary_key=True 指定主键
    auth = models.OneToOneField(to=User,on_delete=models.CASCADE) # ForeignKey ManyToManyField 
    sex = models.SmallIntegerField(choices=Sex.choices, default=Sex.SECRET)
    birthday = models.DateField(verbose_name="出生日期",null=True,blank=True)
    email = models.EmailField(verbose_name="绑定邮箱",unique=True)
 
    def __str__(self) -> str:
        return self.auth.username  