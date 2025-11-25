from django.db import models
from django.db.models import ForeignKey
from django.urls import reverse


class News(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField(blank=True, verbose_name="Контент")
    image = models.ImageField(upload_to='img/%Y/%m/%d/', blank=True, verbose_name="Изображение")
    time_news = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    time_up = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    is_published = models.BooleanField(default=True, verbose_name="Загружено")
    cat = models.ForeignKey("NewsCategory", on_delete=models.PROTECT, verbose_name="Категория")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news', kwargs={'news_slug': self.slug})

    class Meta:
        verbose_name = "игровую новость"
        verbose_name_plural = "новости игр"
        ordering = ["-time_news"]


class NewsCategory(models.Model):
    name = models.CharField(max_length=200, verbose_name="Категория")
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = "игровую категорию"
        verbose_name_plural = "игровые категории"
