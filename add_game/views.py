from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def add_game(response):
    return render(response, './add_game.html')
