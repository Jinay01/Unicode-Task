from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import solution

# Create your views here.
from .models import Newnums
from .forms import *


def home(request):
    context = {}
    return render(request, 'attempt1/main.html', context)


def form(request):
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
