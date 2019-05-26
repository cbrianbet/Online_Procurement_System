from django.contrib.auth import authenticate, login, logout
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
                    if request.user.profile.account_type == 'Bidder':
                        return render(request, 'home/bidderLanding.html')
                    elif request.user.profile.account_type == 'Buyer':
                        return render(request, 'home/buyerLanding.html')
                    else:
                        return render(request, "login/login.html", {'form': form})
                else:
                    return HttpResponse('Account is Disabled')
            else:
                return form.errors('Invalid Credentials')
    else:
        form = LoginForm()
    return render(request, "login/login.html", {'form': form})


def logout_request(request):
    logout(request)
    form = LoginForm()
    messages.info(request, "User is logged out")
    return render(request, 'login/login.html', {'form': form})
