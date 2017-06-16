from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
 
class RegisterForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    password_again = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField(label='Email')
