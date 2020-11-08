from django.contrib import admin
from django.contrib.admin import register

from .models import Post, Tag

@register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
         'title',
        'body',    )
@register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = [
        'title'
    ]

# Register your models here.
