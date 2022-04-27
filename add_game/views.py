from django.shortcuts import render, redirect
from .forms import AddGameForm
from library.views import library
from django.contrib import messages


def add_game(request):
    if request.method == 'POST':
        form = AddGameForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Game successfully added")
            return redirect(library)
        else:
            messages.error(request, "There was a problem adding this game. Please try again")
    form = AddGameForm()
    template = 'add_game/add_game.html'
    context = {
        'form': form
    }
    return render(request, template, context)
