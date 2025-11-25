from .models import *

menu = [
    {'title': '', 'url_name': 'register'},
]


class DataMixin:
    paginate_by = 12

    def get_user_context(self, **kwargs):
        context = kwargs
        cats = NewsCategory.objects.all()

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(0)

        context['menu'] = menu
        context['cats'] = cats

        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context
