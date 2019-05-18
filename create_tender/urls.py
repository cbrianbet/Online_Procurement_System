from django.urls import path
from . import views

urlpatterns = [
    path("tender", views.index, name="create_tender"),
]