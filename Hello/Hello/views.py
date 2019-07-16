from django.shortcuts import render, render_to_response

def dashboard(request):
    return render_to_response('tables.html')
    