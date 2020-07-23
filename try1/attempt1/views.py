from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import solution
import json

# Create your views here.
from .models import Newnums
from .forms import *
import requests


def home(request):
    context = {}
    return render(request, 'attempt1/main.html', context)


def binaryform(request):
    form = Takenums()
    if request.method == "POST":
        form = Takenums(request.POST)
        if form.is_valid:
            form.save()
            return redirect('result')

    context = {'form': form}
    return render(request, 'attempt1/form.html', context)


def binary(request):
    numb = Newnums.objects.last()
    n = numb.numb1
    m = numb.numb2

    dict = solution.solution(n, m)

    context = {'dict': dict}
    return render(request, 'attempt1/result.html', context)


def apiform(request):
    form = Apiform()
    if request.method == "POST":
        form = Apiform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('api')

    context = {'form': form}
    return render(request, 'attempt1/apiform.html', context)


def api(request):
    username = Apiinput.objects.last()
    username = username.username

    # API FOR LIST OF REPOSITORY
    response = requests.get("https://api.github.com/users/" +
                            username + '/repos')
    repository = []
    response = response.json()
    for repos in response:
        repository.append(repos['name'])

    # API FOR LIST OF FOLLOWERS
    response = requests.get(
        'https://api.github.com/users/' + username + "/followers")
    response = response.json()
    followers = []
    for repos in response:
        followers.append(repos['login'])

    # API FOR LIST OF FOLLOWING
    response = requests.get(
        'https://api.github.com/users/' + username + "/following")
    response = response.json()
    following = []
    for repos in response:
        following.append(repos['login'])

    context = {'response': response,
               'repository': repository, 'followers': followers, 'following': following}
    return render(request, 'attempt1/api.html', context)

# 'Jinay01/followers'
# 'following_url': 'https://api.github.com/users/Jinay01/following{/other_user}'
