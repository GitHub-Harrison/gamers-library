from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import Post


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
