from django.shortcuts import render
from django.http import HttpResponse
from library.views import library
from library.models import Post


def home(response):
    posts = Post.objects.filter(approved=True)
    context = {
        'posts': posts,
    }
    return render(response, './home.html', context)
