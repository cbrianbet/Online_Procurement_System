from django.shortcuts import render, redirect


# Create your views here.


def buyerHome(request):

    return render(request, "home/buyerLanding.html")


def bidderHome(request):
    return render(request, "home/bidderLanding.html")
