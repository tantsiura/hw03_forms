from django.core.paginator import Paginator

from .models import QUANTITY_POSTS


def get_page_context (request, posts):
    paginator = Paginator(posts, QUANTITY_POSTS)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj
