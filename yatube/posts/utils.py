from django.conf import global_settings
from django.core.paginator import Paginator


def get_page_of_paginator(request, posts):
    paginator = Paginator(posts, global_settings.characters_in_post)
    page_number = request.GET.get('page')
    return paginator.get_page(page_number)
