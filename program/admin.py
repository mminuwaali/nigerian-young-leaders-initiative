from . import models
from django.contrib import admin


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    list_display = ["name", "created_at", "updated_at"]


@admin.register(models.Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ["title", "created_at", "updated_at"]
