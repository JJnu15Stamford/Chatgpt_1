from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegisterForm

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # log the user in after successful registration
            return redirect("book_list")  # or any other page
    else:
        form = RegisterForm()
    return render(request, "library/register.html", {"form": form})
