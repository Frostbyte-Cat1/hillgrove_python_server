from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    print(request)
    return HttpResponse('Hello world! Authentication APIs with Google goes ')


def signup(request):
    pass
