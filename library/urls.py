from django.urls import path
from . import views

urlpatterns = [
    path('library/', views.library, name='library'),
    path('<slug:slug>/', views.library, name='post_detail'),
]
