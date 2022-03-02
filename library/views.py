from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def library(response):
    return render(response, './library.html')
