from django.core.paginator import Paginator

from .models import QUANTITY_POSTS


def get_page_of_paginator(request, posts):
    paginator = Paginator(posts, QUANTITY_POSTS)
    page_number = request.GET.get('page')
    return paginator.get_page(page_number)
