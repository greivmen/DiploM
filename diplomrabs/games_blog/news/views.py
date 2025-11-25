from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .models import *
from .forms import *
from .utils import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login


class NewsBlogHome(DataMixin, ListView):
    model = News
    template_name = "news/index.html"
    context_object_name = "posts"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['title'] = "Главан страница"
        # context['menu'] = menuсвcсв
        # context['cat_selected'] = 0
        fec = self.get_user_context(title="ВСЕ")
        return dict(list(context.items()) + list(fec.items()))

    def get_queryset(self):
        return News.objects.filter(is_published=True).select_related('cat')


class ShowNews(DataMixin, DetailView):
    model = News
    template_name = "news/post.html"
    context_object_name = "post"
    slug_url_kwarg = "news_slug"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['title'] = context['post']
        # context['menu'] = menu
        fec = self.get_user_context(title='post')
        return dict(list(context.items()) + list(fec.items()))


class BlogCategory(DataMixin, ListView):
    model = News
    template_name = "news/index.html"
    context_object_name = "posts"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Категория - " + str(context['posts'][0].cat)
        context['menu'] = menu
        context['cat_selected'] = context['posts'][0].cat_id
        return context

    def get_queryset(self):
        return News.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True).select_related('cat')


class RegisterUser(DataMixin, CreateView):
    form_class = Register
    template_name = 'news/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        fec = self.get_user_context(title='Регистрация')
        return dict(list(context.items()) + list(fec.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')


class LoginUser(DataMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'news/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        fec = self.get_user_context(title='Авторизация')
        return dict(list(context.items()) + list(fec.items()))
