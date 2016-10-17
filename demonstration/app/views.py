from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('Hello World!')