from django.urls import path
from django.conf.urls import url
from . import views
from create_bids import views as bid_view

urlpatterns = [
    path('tender', views.index, name="create_tender"),
    url(r'^bid/$', bid_view.index),
]
