from django.forms import ModelForm
from .models import UserFileUpload
from django import forms

# A form used to setup the file upload system.
class UploadFileForm(ModelForm):
    class Meta:
        model = UserFileUpload # creates the model UserFileUpload
        fields = ['upload'] # Defines the field 'upload'
        widgets = { # Styles the form to give it a more appearling design. Extended on the template.
            "upload": forms.ClearableFileInput(
                attrs={
                    'size':'30',
                    'style':'position:relative; z-index: 100; padding-top:10px; padding-bottom:10px; padding-left:17%; padding-right:17%; line-height: 0px;',
                }),
        } 