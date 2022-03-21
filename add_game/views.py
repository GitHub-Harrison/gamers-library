from django.shortcuts import render, redirect
from .forms import AddGameForm
from library.views import library


def add_game(request):
    if request.method == 'POST':
        form = AddGameForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(library)
    form = AddGameForm()
    template = 'add_game/add_game.html'
    context = {
        'form': form
    }
    return render(request, template, context)
