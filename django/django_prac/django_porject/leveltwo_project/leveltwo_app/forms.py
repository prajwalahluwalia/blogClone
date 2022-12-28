from dataclasses import fields
from importlib.metadata import files
from django import forms
from django.core import validators
from leveltwo_app.models import User

class NewUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
    