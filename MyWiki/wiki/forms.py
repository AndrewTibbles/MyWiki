from django.forms import ModelForm
from .models import UserFileUpload
from django import forms


class UploadFileForm(ModelForm):
    class Meta:
        model = UserFileUpload
        fields = ['upload']
        widgets = {
            "upload": forms.ClearableFileInput(
                attrs={
                    'size':'30',
                    'style':'position:relative; z-index: 100; padding-top:10px; padding-bottom:10px; padding-left:17%; padding-right:17%; line-height: 0px;',
                }),
        } 