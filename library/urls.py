from django.urls import path
from . import views

urlpatterns = [
    path('library/', views.library, name='library'),
    path('<slug:slug>', views.post_detail, name='post_detail'),
    path(
        'update_comment/<int:id>',
        views.update_comment, name='update_comment'),
    path('edit_comment/<int:id>', views.edit_comment, name='edit_comment'),
    path(
        'delete_comment/<int:id>',
        views.delete_comment, name='delete_comment'),

]
