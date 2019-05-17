from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


def index(request):
    return render(request, "login/login.html")


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = UserCreationForm()
        args = {'form': form}
        return render(request, "login/test.html", args)


def success(request):
    return render(request, "login/success.html")
