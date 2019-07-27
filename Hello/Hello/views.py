from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import Context
from django.template.loader import get_template
# from .models import *
# from . forms import *
from django.template.context_processors import csrf
from copy import deepcopy
from datetime import datetime as dt
import datetime


def dashboard(request):
    return render_to_response('SIH.html')


def main(request):
    return HttpResponse("OK")


def Text_To_Speech(request):
    return render_to_response('Text_To_Sign.html')


def our_products(request):
    return render_to_response('our_products.html')


def convert(request):
    if request.GET:
        Text = request.GET.get('search')
        print(Text.split())
        return render_to_response('Text_To_Sign.html')
