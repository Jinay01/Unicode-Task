from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import solution
import json

# Create your views here.
from .models import *
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
    custom_list = []
    objec = Apiinput.objects.all()
    for i in objec:
        if i.username not in custom_list:
            custom_list.append(i.username)
    form = Apiform()
    if request.method == "POST":
        form = Apiform(request.POST)
        if form.is_valid():
            user = form.cleaned_data['username']
            if user in custom_list:
                i = Apiinput.objects.get(username=user)
                i.counter = i.counter + 1
                i.save()
            else:
                form.save()
        return api(request, user)
    context = {'form': form}
    return render(request, 'attempt1/apiform.html', context)


def api(request, user):
    x = Apiinput.objects.get(username=user)
    username = x.username

    # API FOR LIST OF REPOSITORY
    response = requests.get("https://api.github.com/users/" +
                            username + '/repos')
    repository = []
    response = response.json()
    for repos in response:
        repository.append(repos['name'])
    # Repository counter
    repository_count = 0
    for i in repository:
        repository_count += 1
    x.repo_count = repository_count
    x.save()
    # API FOR LIST OF FOLLOWERS
    response = requests.get(
        'https://api.github.com/users/' + username + "/followers")
    response = response.json()
    followers = []
    for repos in response:
        followers.append(repos['login'])
    # Followers counter
    followers_count = 0
    for i in followers:
        followers_count += 1
    x.followers_count = followers_count
    x.save()

    # API FOR LIST OF FOLLOWING
    response = requests.get(
        'https://api.github.com/users/' + username + "/following")
    response = response.json()
    following = []
    for repos in response:
        following.append(repos['login'])
    # Following counter
    following_count = 0
    for i in following:
        following_count += 1
    x.following_count = following_count
    x.save()

    context = {'response': response,
               'repository': repository, 'followers': followers, 'following': following, 'followers_count': followers_count, 'following_count': following_count, 'repository_count': repository_count, }
    return render(request, 'attempt1/api.html', context)

# 'Jinay01/followers'
# 'following_url': 'https://api.github.com/users/Jinay01/following{/other_user}'


def userfinder(request):
    context = {}
    return render(request, 'attempt1/userfinder.html', context)


def repofinder(request):
    user = ''
    li = []
    form = Repofinder()
    if request.method == 'POST':
        form = Repofinder(request.POST)
        if form.is_valid():
            repo = form.cleaned_data['repo_count']
            i = Apiinput.objects.filter(repo_count=repo)
            for x in i:
                li.append(x.username)
            user = li
    context = {'form': form, 'user': user}
    return render(request, 'attempt1/repofinder.html', context)


def followersfinder(request):
    user = ''
    li = []
    form = Followersfinder()
    if request.method == 'POST':
        form = Followersfinder(request.POST)
        if form.is_valid():
            repo = form.cleaned_data['followers_count']
            i = Apiinput.objects.filter(followers_count=repo)
            for x in i:
                li.append(x.username)
            user = li
    context = {'form': form, 'user': user}
    return render(request, 'attempt1/followersfinder.html', context)


def followingfinder(request):
    user = ''
    li = []
    form = Followingfinder()
    if request.method == 'POST':
        form = Followingfinder(request.POST)
        if form.is_valid():
            repo = form.cleaned_data['following_count']
            i = Apiinput.objects.filter(following_count=repo)
            for x in i:
                li.append(x.username)
            user = li
    context = {'form': form, 'user': user}
    return render(request, 'attempt1/followingfinder.html', context)


def top(request):
    lis = []
    high = []
    se = set()
    high1 = []
    high2 = []
    high3 = []
    i = Apiinput.objects.all()
    for b in i:  # This steps are done on purpose if 2 have same value to uske liye difficult to explain
        lis.append(b.counter)  # But donot remove this coz ye kaamka hai
    lis.sort()
    for a in lis:
        se.add(a)
    for c in se:
        high.append(c)
    high.sort()
    high.reverse()

    obj1 = Apiinput.objects.filter(counter=high[0])
    for z in obj1:
        high1.append(z.username)
    obj2 = Apiinput.objects.filter(counter=high[1])
    for y in obj2:
        high2.append(y.username)
    obj3 = Apiinput.objects.filter(counter=high[2])
    for x in obj3:
        high3.append(x.username)

    context = {'high1': high1, 'high2': high2, 'high3': high3}
    return render(request, 'attempt1/top.html', context)
