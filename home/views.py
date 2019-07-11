from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


# Create your views here.

@login_required
def buyerHome(request):
    return render(request, "home/buyerLanding.html")


@login_required
def bidderHome(request):
    return render(request, "home/bidderLanding.html")


@login_required
def help(request):
    return render(request, "home/help.html")
