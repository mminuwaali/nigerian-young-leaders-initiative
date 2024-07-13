from . import models
from account.models import Team
from django.contrib import messages
from account.forms import ContactForm
from program.models import Program,Category
from django.shortcuts import render, redirect


def index_view(request):
    categories = Category.objects.all()

    context = {"categories":categories}
    return render(request, "landing/index.html", context)


def about_view(request):
    return render(request, "landing/about.html")


def donate_view(request):
    if request.method == "POST":
        messages.info(request, "It's under construction")
        return redirect("landing:donate-view")

    return render(request, "landing/donate.html")


def apply_view(request):
    programs = Program.objects.all()

    context = {"programs": programs}
    return render(request, "landing/apply.html", context)


def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid() and form.save():
            messages.success(request, "Form sumitted successfylly")

        else:
            messages.error(request, "Something went wrong!")
        return redirect("landing:contact-view")
    return render(request, "landing/contact.html")


def student_view(request):
    students = models.Student.objects.all()

    context = {"students": students}
    return render(request, "landing/student.html", context)


def team_view(request):
    teams = Team.objects.all()

    context = {"teams": teams}
    return render(request, "landing/team/index.html", context)


def team_detail_view(request, id):
    team = Team.objects.get(id=id)

    context = {"team": team}
    return render(request, "landing/team/detail.html", context)
