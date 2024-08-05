from uuid import uuid4
from django.db import models
from markdownx.utils import markdownify
from markdownx.models import MarkdownxField


class Category(models.Model):
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.name.title()


class Program(models.Model):
    description = MarkdownxField(default="")
    title = models.CharField(max_length=255)
    summary = models.CharField(max_length=2000)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="programs", blank=True)
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    category = models.ForeignKey(Category, models.PROTECT, null=True, blank=True)

    @property
    def content(self):
        return markdownify(self.description)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title.title()


class Application(models.Model):
    program = models.ForeignKey(Program, models.PROTECT)
