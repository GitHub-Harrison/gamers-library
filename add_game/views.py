from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import AddGameForm
from library.views import library
from library.models import Post


@login_required
def add_game(request):
    if request.method == 'POST':
        form = AddGameForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            messages.success(request, "Game successfully added")
            return redirect(library)
        else:
            messages.error(
                request,
                "There was a problem adding this game. Please try again")
    form = AddGameForm()
    template = 'add_game/add_game.html'
    context = {
        'form': form
    }
    return render(request, template, context)


@login_required
def update_game(request, id):
    game = get_object_or_404(Post, id=id)
    if not game.user == request.user:
        messages.error(request, "You are not authorised")
        return redirect(library)

    if request.method == 'POST':
        form = AddGameForm(request.POST, request.FILES, instance=game)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            messages.success(request, "Game successfully updated")
            return redirect(library)
        else:
            messages.error(
                request,
                "There was a problem updated this game. Please try again")
    form = AddGameForm(instance=game)
    template = 'add_game/update_game.html'
    context = {
        'form': form,
        'game': game,
    }
    return render(request, template, context)


@login_required
def delete_game(request, id):
    game = get_object_or_404(Post, id=id)
    if not game.user == request.user:
        messages.error(request, "You are not authorised")
        return redirect(library)

    messages.success(request, "Game successfully deleted")
    game.delete()
    return redirect(library)
