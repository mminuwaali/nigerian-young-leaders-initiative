from . import models
from django.contrib import admin


@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    list_filter = ["program"]
    list_display = ["name", "program", "created_at", "updated_at"]
