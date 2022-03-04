from django.urls import path

from . import views

urlpatterns = [
    path('add_game/', views.add_game, name='add_game'),
]
