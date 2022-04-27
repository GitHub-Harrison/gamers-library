from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import View
from django.core.paginator import Paginator
from .models import Post
from .forms import CommentForm
from django.contrib import messages


def library(response):
    posts = Post.objects.filter(approved=True)

    post_paginator = Paginator(posts, 3)
    page_num = response.GET.get('page')
    page = post_paginator.get_page(page_num)

    template = 'library/library.html'
    context = {
        'page': page,
        'count': post_paginator.count
    }

    return render(response, template, context)


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
            messages.success(request, "Your comment has been added")
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
