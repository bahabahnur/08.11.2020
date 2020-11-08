from django.contrib import admin
from django.contrib.admin import register

from .models import Post

@register(Post)
class CarAdmin(admin.ModelAdmin):
    list_display = (
         'title',
        'body',    )

# Register your models here.
