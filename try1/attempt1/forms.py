from django.forms import ModelForm
from django import forms
from .models import *


class Takenums(ModelForm):
    class Meta():
        model = Newnums
        fields = '__all__'
