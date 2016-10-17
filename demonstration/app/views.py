from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse
import json
import requests
# Create your views here.

def index(request):
    return HttpResponse('Hello World!')

def test(request):
    return HttpResponse('My second view!')

def profile(request):
    req=requests.get('https://api.github.com/users/kelvinkipsang')
    content = req.text
    return HttpResponse(content)