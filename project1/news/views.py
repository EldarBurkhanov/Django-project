from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    print(request)
    return HttpResponse('Hello world')


def testing_page(request):
    print(request)
    return HttpResponse('Testing page')