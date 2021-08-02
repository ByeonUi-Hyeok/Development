from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'animal/main.html', {})


def companion(request):
    return render(request, 'animal/companion/companion.html', {})


def ownerless(request):
    return render(request, 'animal/ownerless/ownerless.html', {})

def status(request):
    return render(request, 'animal/ownerless/status.html', {})

def others(request):
    return render(request, 'animal/ownerless/others.html', {})