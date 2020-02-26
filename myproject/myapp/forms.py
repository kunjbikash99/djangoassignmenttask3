from django import forms
from django.db import models
from .models import login,already,Blog
from django.core import validators

class loginform(forms.ModelForm):
    class Meta:
        model=login
        fields="__all__"

class alreadyf(forms.ModelForm):
    class Meta:
        model=already
        fields="__all__"

class Blogf(forms.ModelForm):
    class Meta:
        model=Blog
        fields="__all__"

