from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def library(response):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(response, './library.html', context)

def add_game(response):
    return render(response, './add_game.html')
