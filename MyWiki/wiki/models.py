from django.db import models
from django.urls import reverse
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class Page(models.Model):
    title = models.CharField(max_length=64, primary_key=True) # Defines the pages title and applies parameters to limit word count and to make it the primary field of the database.
    content = models.TextField() # Adds a text field for the pages content. No extra parameters are needed for this at this time.
    counter = models.IntegerField(default=1) # defines the word counter using interger values which is default to 1. This will be saved to the database and will record a pages visits.

    
    def __str__(self):
        return self.title # returns the title.

    def get_absolute_url(self):
        return reverse('wiki:detail', args=[self.title]) # Proviedes the detail view with the args 'title'

# User form for members to signup.
class SignUpForm(UserCreationForm):

    # Adds a character field to the form with a label, max length, help text and a placeholder.
    username = forms.CharField(label='Username', max_length=30, required=True, help_text='Please choose a username.', widget=forms.TextInput(attrs={'placeholder': 'Username'})) 
    first_name = forms.CharField(label='Forename', max_length=30, required=False, help_text='Optional.') # Adds a character field to the form with a label, max length and some help text.
    last_name =  forms.CharField(label='Surname', max_length=30, required=False, help_text='Optional.' )# Adds a character field to the form with a label, max length and some help text.
    email =      forms.EmailField(label='Email', max_length=254, required=True, help_text='Required. Inform a valid email address.') # Adds a character field to the form with a label, max length and some help text.
    password1 =  forms.CharField(label='Password', max_length=30, required=True, help_text='Required.') # Adds a character field to the form with a label, max length and some help text.
    password2 =  forms.CharField(label='Confirm Password', max_length=30, required=True, help_text='Required.') # Adds a character field to the form with a label, max length and some help text.

    class Meta:
        model = User # Defines a model 'User'
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', ]

class UserFileUpload(models.Model):
    upload = models.FileField(upload_to='upload/') # Defines a file field for use on the forms.py and the file upload page.

    def __str__(self):
        return self.upload.name # returns the upload name