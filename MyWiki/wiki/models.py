from django.db import models
from django.urls import reverse
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class Page(models.Model):
    title = models.CharField(max_length=64, primary_key=True)
    content = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('wiki:detail', args=[self.title])

class SignUpForm(UserCreationForm):

    username = forms.CharField(label='Username', max_length=30, required=True, help_text='Please choose a username.', widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    first_name = forms.CharField(label='Forename', max_length=30, required=False, help_text='Optional.')
    last_name =  forms.CharField(label='Surname', max_length=30, required=False, help_text='Optional.')
    email =      forms.EmailField(label='Email', max_length=254, required=True, help_text='Required. Inform a valid email address.')
    password1 =  forms.CharField(label='Password', max_length=30, required=True, help_text='Required.')
    password2 =  forms.CharField(label='Confirm Password', max_length=30, required=True, help_text='Required.')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', ]