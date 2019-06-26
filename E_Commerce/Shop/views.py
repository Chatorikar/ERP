from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Index Shop")

# Create your views here.
