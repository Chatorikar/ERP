from django.shortcuts import render, render_to_response


def dashboard(request):
    return render_to_response('dashboard.html')


def our_products(request):
    return render_to_response('our_products.html')
