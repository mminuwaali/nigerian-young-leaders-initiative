from uuid import uuid4
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Category(models.Model):
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255, unique=True)
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name.title()


class Blog(models.Model):
    content = models.TextField()
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, models.CASCADE)
    image = models.ImageField(default="", upload_to="blog-posts")
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title.title()
