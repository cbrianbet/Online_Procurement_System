from django.urls import path
from django.conf.urls import url
from . import views
from create_bids import views as bid_view

urlpatterns = [
    path('tender', views.index, name="create_tender"),
    path('list', views.tenderlist),
    url(r'^bid/$', bid_view.bidlist, name='bid_feed'),
    url(r'^bid_history/$', bid_view.my_bids, name='bid_history'),
    path('bid<int:tender_id>', bid_view.index, name='bid_tender'),
]
