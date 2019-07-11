from django.urls import path
from . import views

urlpatterns = [
    path("buyerHome", views.buyerHome, name="buyerHome"),
    path("bidderHome", views.bidderHome, name="bidderHome"),
    path("help", views.help, name="help"),
]
