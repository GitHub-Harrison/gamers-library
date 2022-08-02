from django.urls import path

from . import views

urlpatterns = [
    path('add_game/', views.add_game, name='add_game'),
    path('update_game/<int:id>/', views.update_game, name='update_game'),
    path('delete_game/<int:id>/', views.delete_game, name='delete_game'),
]
