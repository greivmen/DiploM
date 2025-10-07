from django.shortcuts import render
from django.views.generic import ListView
from .models import *


class NewsBlogHome(ListView):
    model = News
    template_name = "news/index.html"
    context_object_name = "posts"
