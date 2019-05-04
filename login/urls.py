from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="login"),
    path("register", views.signup, name="signup"),
    path("register/success", views.success, name="success"),
]
