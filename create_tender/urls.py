from django.urls import path
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from . import views
from create_bids import views as bid_view

urlpatterns = [
    # Seller Urls and paths
    path('desktop_tender', views.index, name="create_tender"),
    path('const_tender', views.const_tender, name="constTender"),
    path('list', views.tenderlist),
    url(r'^tender_history/$', views.my_tenders, name='tender_history'),
    url(r'^tenderType/$', views.tender_type, name='tenderType'),
    path('tender_delete<int:pk>/', views.del_tender, name='del_tender'),
    path('acc_bid_info<int:bid_id>/', views.acc_list, name='acc_bid_info'),
    # Bidder Urls and paths
    url(r'^bid/$', bid_view.tender_list, name='tender_feed'),
    url(r'^bid_history/$', bid_view.my_bids, name='bid_history'),
    path('bid<int:tender_id>', bid_view.index, name='bid_tender'),
    path('bidview<int:bids_id>', bid_view.bid_update, name='bid_update'),
    path('bidedit<int:bids_id>', bid_view.bid_edit, name='bid_edit'),
    path('biddelete<int:pk>/', bid_view.del_bid, name='del_bid'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
