from django.shortcuts import render
from django.http import HttpResponse
# from .forms import AddGameForm

# Create your views here.


# def post_game(request):
#     if request.method == 'POST':
#         form = AddGameForm(request.POST)
#         if form.is_valid():
#             return HttpResponseRedirect('/library/')


def add_game(response):
    return render(response, './add_game.html')
