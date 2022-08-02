from django.contrib import admin
from .models import Post, Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('user', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'title', 'genre', 'platform', 'release_date',
        'approved', 'created_on')
    list_filter = ('approved', 'genre', 'platform')
    search_fields = ('user', 'description', 'title')


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
