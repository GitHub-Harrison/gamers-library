from django.shortcuts import render
from django.http import HttpResponse
from library.views import library
from library.models import Post


def home(response):
    return render(response, './home.html')


# def home(response):
#     template = 'home/home.html'
#     context = {}
#     return render(response, template, context)
