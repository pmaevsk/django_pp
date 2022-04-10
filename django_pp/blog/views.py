from multiprocessing import context
from django.shortcuts import render

posts = [
    {
        'author': 'PMaevski',
        'title': 'Blog Post 1',
        'content': 'First blog post ever',
        'date_posted': 'April 10, 2022'
    },
    {
        'author': 'TestUser',
        'title': 'Blog Post 2',
        'content': 'Some test text',
        'date_posted': 'April 9, 2022'
    },
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
# Create your views here.
