from django.shortcuts import render
from django.http import HttpResponse


def home(response):
    return render(response, './home.html')


# def home(response):
#     template = 'home/home.html'
#     context = {}
#     return render(response, template, context)
