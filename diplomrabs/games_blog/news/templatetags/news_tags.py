from django import template
from news.models import *

register = template.Library()


@register.inclusion_tag('news/list_categories.html')
def show_categories(sort=None, cat_selected=0):
    if not sort:
        cats = NewsCategory.objects.all()
    else:
        cats = NewsCategory.objects.order_by(sort)

    return {"cats": cats, "cat_selected": cat_selected}
