from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser): ...


class Contact(models.Model):
    email = models.EmailField()
    message = models.TextField()
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]


class Newsletter(models.Model):
    name = models.CharField(max_length=255)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(max_length=255, unique=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.name.title()


class Team(models.Model):
    position = models.CharField(max_length=255)
    about = models.TextField(default="", blank=True)
    user = models.OneToOneField(User, models.CASCADE)
    image = models.ImageField(default="", upload_to="teams")

    def __str__(self):
        return self.user.username
