from django.shortcuts import render
from django.http import HttpResponse # No need for this import as we use shortcut render that returns a HttpResponse

# Create your views here.

posts = [
    {
        'author': 'JunePyo',
        'title':'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'John Fish',
        'title':'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2018'
    },
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})