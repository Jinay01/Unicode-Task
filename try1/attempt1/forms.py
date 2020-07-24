from django.forms import ModelForm
from django import forms
from .models import *


class Takenums(ModelForm):
    class Meta():
        model = Newnums
        fields = '__all__'


class Apiform(ModelForm):
    class Meta():
        model = Apiinput
        fields = ['username']


# class Usercount(ModelForm):
#     class Meta():
#         model = Usercheck
#         fields = '__all__'

class Repofinder(ModelForm):
    class Meta():
        model = Apiinput
        fields = ['repo_count']


class Followersfinder(ModelForm):
    class Meta():
        model = Apiinput
        fields = ['followers_count']


class Followingfinder(ModelForm):
    class Meta():
        model = Apiinput
        fields = ['following_count']
