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


# class PostDetail(View):
#     def get(self, request, slug, *args, **kwargs):
#         queryset = Post.objects.filter(status=1)
#         post = get_object_or_404(queryset, slug=slug)

#         template = 'library/post_detail.html'
#         context = {
#             'post': post,
#         }

#         return render(request, template, context)


def post_detail(request, slug):

    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    template = 'library/post_detail.html'

    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object
            new_comment = comment_form.save(commit=False)
            # Assign current post to comment
            new_comment.post = post
            # Save comment to database
            new_comment.save()

    else:
        comment_form = CommentForm()

    context = {
        'post': post,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form
    }

    return render(request, template, context)
