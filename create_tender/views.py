from django.shortcuts import render, redirect


def index(request):
    return render(request, "create_tender/Create.html")
