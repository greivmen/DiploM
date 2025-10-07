from django.urls import path
from .views import *


urlpatterns = [
    path('', NewsBlogHome.as_view(), name='index')
]
