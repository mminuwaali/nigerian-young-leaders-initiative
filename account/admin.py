from . import models
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


@admin.register(models.User)
class UserAdmin(BaseUserAdmin): ...


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display_links = ["name"]
    list_display = ["name", "email"]
    search_fields = ["name", "email"]


@admin.register(models.Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display_links = ["name"]
    list_display = ["name", "email"]
    search_fields = ["name", "email"]


@admin.register(models.Team)
class TeamAdmin(admin.ModelAdmin):
    list_display_links = ["user"]
    list_display = ["user", "position", "about"]
