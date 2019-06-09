from django.urls import path
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from . import views
from create_bids import views as bid_view

urlpatterns = [
    # Seller Urls and paths
    path('tender', views.index, name="create_tender"),
    path('list', views.tenderlist),
    url(r'^tender_history/$', views.my_tenders, name='tender_history'),
    # Bidder Urls and paths
    url(r'^bid/$', bid_view.tender_list, name='tender_feed'),
    url(r'^bid_history/$', bid_view.my_bids, name='bid_history'),
    path('bid<int:tender_id>', bid_view.index, name='bid_tender'),
    path('bidupdate<int:bids_id>', bid_view.bid_update, name='bid_update'),
    path('biddelete<int:pk>/', bid_view.del_bid, name='del_bid'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
