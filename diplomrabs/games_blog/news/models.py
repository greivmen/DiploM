from django.db import models
from django.db.models import ForeignKey


class News(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField(blank=True)
    image = models.ImageField(upload_to='img/%Y/%m/%d/', blank=True)
    time_news = models.DateTimeField(auto_now_add=True)
    time_up = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey("NewsCategory", on_delete=models.PROTECT)

    def __str__(self):
        return self.title


class NewsCategory(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.name
