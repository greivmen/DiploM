from django.contrib import admin
from .models import *

from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms


class AdminObraz(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = News
        fields = "__all__"


class BlogAdmin(admin.ModelAdmin):
    form = AdminObraz
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('id', 'title', 'cat', 'time_news', 'image', 'is_published')
    list_display_links = ('id', 'title', 'time_news')
    search_fields = ('title', 'content')
    list_filter = ('is_published', 'time_news')
    list_editable = ('is_published',)


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


admin.site.register(News, BlogAdmin)
admin.site.register(NewsCategory, CategoryAdmin)
