# from django.contrib.auth.models import User
from django import forms


class Register(forms.ModelForm):
    fname = forms.CharField(widget=forms.TextInput(
        attrs={'class': "input", 'size': "40"}))
    lname = forms.CharField(widget=forms.TextInput(
        attrs={'class': "input", 'size': "40"}))
    phone = forms.In
    password = forms.CharField(widget=forms.PasswordInput())
