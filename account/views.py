from . import forms
from django.contrib import auth, messages
from django.shortcuts import render, redirect


def signout_view(request):
    if request.method == "POST":
        auth.logout(request)

    return redirect("account:signin-view")


def signin_view(request):
    if request.method == "POST":
        user = auth.authenticate(
            request,
            username=request.POST.get("username"),
            password=request.POST.get("password"),
        )
        if user:
            auth.login(request, user)
            return redirect("landing:index-view")

        messages.error(request, "Invalid credentials")
    return render(request, "account/signin.html")


def signup_view(request):
    if request.method == "POST":
        form = forms.RegisterForm(request.POST)

        if form.is_valid() and form.save():
            messages.success(request, "Registeration successfull, login now")
            return redirect("account:signin-view")

        (messages.error(request, i) for i in form.errors.values())
        return redirect("account:signup-view")

    return render(request, "account/signup.html")
