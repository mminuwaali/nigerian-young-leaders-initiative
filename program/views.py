from . import models
from django.shortcuts import render


def index_view(request):
    programs = models.Program.objects.all()

    context = {"programs": programs}
    return render(request, "program/index.html", context)


def detail_view(request, id):
    program = models.Program.objects.get(id=id)

    context = {"program": program}
    return render(request, "program/detail.html", context)
