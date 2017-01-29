from django.contrib.auth.models import User
from django import forms
from django.forms import Textarea

class Register(forms.ModelForm):
	fname = forms.CharField(widget = forms.TextInput(attrs = {'class':"input",'size':"40"}))
	lname = forms.CharField(widget = forms.TextInput(attrs = {'class':"input",'size':"40"}))
	password = forms.CharField(widget  = forms.PasswordInput())