from django.urls import path
from . import views

urlpatterns = [
    path('library/', views.library, name='library'),
    path('<slug:slug>', views.post_detail, name='post_detail'),
    path('update_comment/', views.UpdateComment, name='update_comment'),
]
