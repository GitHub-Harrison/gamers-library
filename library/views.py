import re

from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views import View

from .forms import CommentForm
from .models import Comment, Post


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
            messages.success(request, "Your comment is awaiting moderation")
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


def update_comment(request, id):
    # this view returns page with context, and from this page we are editing comment
    comment_obj = get_object_or_404(Comment, id=id)
    comment_form = CommentForm(instance=comment_obj)
    context = {
        'comment': comment_obj,
        "comment_form": comment_form,
    }
    return render(request, "library/update_comment.html", context)


def edit_comment(request, id):
    if request.POST:
        new_body = request.POST.get("body")
        # From post data we are getting data body. and then getting object comment and saving with a new data
        comment_obj = get_object_or_404(Comment, id=id)
        comment_obj.body = new_body
        comment_obj.save()
        messages.success(request, "Your comment is Updated")
    return redirect("library")


def delete_comment(request, id):
    if request.POST:
        url_path = request.POST.get("path")
        # we have created hidden inputs in post_detail.html and from here getting path

        comment_obj = get_object_or_404(Comment, id=id)

        comment_obj.delete()
        messages.success(request, "Your comment is Deleted")

        return redirect(url_path)
