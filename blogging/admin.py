from . import models
from django.contrib import admin


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]


@admin.register(models.Blog)
class BlogAdmin(admin.ModelAdmin):
    list_filter = ["category"]
    search_fields = ["title", "author", "category"]
    list_display = ["title", "author", "category", "created_at"]
