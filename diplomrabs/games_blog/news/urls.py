from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', NewsBlogHome.as_view(), name='index'),
    path('news/<slug:news_slug>/', ShowNews.as_view(), name='news'),
    path('category/<slug:cat_slug>/', BlogCategory.as_view(), name='category'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('exit/',  auth_views.LogoutView.as_view(template_name="news/exit.html"),
         name='exit'),
]
