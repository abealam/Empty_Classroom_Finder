from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(response):
    return render(response, "base.html", {})

def v1(response):
    return render(response, "home.html", {})
