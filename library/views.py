from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import View
from django.core.paginator import Paginator
from .models import Post
from .forms import CommentForm


def library(response):
    posts = Post.objects.all()

    post_paginator = Paginator(posts, 5)
    page_num = response.GET.get('page')
    page = post_paginator.get_page(page_num)

    template = 'library/library.html'
    context = {
        'page': page,
        'count': post_paginator.count
    }

    return render(response, template, context)


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "library/post_detail.html",
            {
                "post": post,
                "comments": comment,
                "liked": liked,
                "comment_form": CommentForm()
            }
        )
