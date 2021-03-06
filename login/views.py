from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import LoginForm


def index(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            clean = form.cleaned_data
            user = authenticate(username=clean['username'], password=clean['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    if request.user.groups.filter(name="admins").exists():
                        return redirect('bidderHome')
                    elif request.user.profile.account_type == 'Buyer':
                        return redirect('buyerHome')
                    else:
                        return render(request, "login/login.html", {'form': form})
                else:
                    return HttpResponse('Account is Disabled')
            else:
                form = LoginForm()
                inv = messages.error(request, "invalid credentials", fail_silently=True)
                return render(request, 'login/login.html', {'form': form, 'messages': inv})
    else:
        form = LoginForm()

    return render(request, "login/login.html", {'form': form})


def logout_request(request):
    logout(request)
    messages.info(request, "User is logged out", fail_silently=True)
    return redirect('login')
