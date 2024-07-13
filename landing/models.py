from django.db import models
from program.models import Program


# Create your models here.
class Event(models.Model):
    image = models.ImageField(upload_to="events")


class Student(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="students")
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    program = models.ForeignKey(Program, models.CASCADE)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.name.title()
