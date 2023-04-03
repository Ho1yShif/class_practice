from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
    'author': 'Shif',
    'title': 'First Blog Post!',
    'content': 'The first post inside my first Django project :)',
    'date_posted': 'March 22, 2023'
    },
    {
    'author': 'Pro Grammar',
    'title': 'Coding',
    'content': 'I am a professional grammar.',
    'date_posted': 'March 21, 2023'
    }
]

def home(request):
    # Access post information above through this keyname
    context = {'posts': posts}
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
