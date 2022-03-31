from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import Post


def library(response):
    posts = Post.objects.all()

    # changing get_page() works but doesn't work via the next button on webpage
    post_paginator = Paginator(posts, 5)
    page_num = response.GET.get('page')
    page = post_paginator.get_page(1)

    template = 'library/library.html'
    context = {
        'page': page,
        'count': post_paginator.count
    }

    return render(response, template, context)
