from django import forms
from .models import *

class DataCollectForm(forms.ModelForm):
    class Meta:
        model = FieldData
        fields = ["owner","str_data","int_data","file_data"]
