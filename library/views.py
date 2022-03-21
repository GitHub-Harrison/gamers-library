from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def library(response):
    posts = Post.objects.all()
    template = 'library/library.html'
    context = {
        'posts': posts
    }
    return render(response, template, context)
