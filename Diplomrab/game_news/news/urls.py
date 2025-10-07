from django.urls import path
from .views import *

urlpatterns = [
    path('', GameHome.as_view(), neme='index'),
]
