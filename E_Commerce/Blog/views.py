from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author' : 'Prathamesh',
        'title' : 'ACP',
        'date' : '2021'
    }
    ,
     
    {
        'author' : 'Chatorikar',
        'title' : 'DCP',
        'date' : '2027'
    }

]


def home(request):
    context = {
        'posts' : posts
    }
    return render(request,'Blog/home.html' , context)
    #return HttpResponse("<h1>Blog Home</h1>")

def about(request):
    return render(request,'Blog/about.html',{'title' : 'About'})
# Create your views here.
