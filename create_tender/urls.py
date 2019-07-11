from django.urls import path
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from . import views
from create_bids import views as bid_view

urlpatterns = [
    # Seller Urls and paths
    path('desktop_tender', views.index, name="desktp_tender"),
    path('const_tender', views.const_tender, name="constTender"),
    path('furn_tender', views.furn_tender, name="furnitureTender"),
    url(r'^tender_history/$', views.my_tenders, name='tender_history'),
    url(r'^tender_historya/$', views.my_tenders_a, name='tender_historyA'),
    url(r'^tenderType/$', views.tender_type, name='tenderType'),
    path('tender_delete<int:pk>/', views.del_tender, name='del_tender'),
    path('tenderedit<int:tender_id>', views.tender_edit, name='tenderEdit'),
    path('furnedit<int:tender_id>', views.furn_tender_edit, name='furnEdit'),
    path('constedit<int:tender_id>', views.const_tender_edit, name='constEdit'),
    path('fullrep', views.aw_rep, name='awRep'),

    # Bidder Urls and paths
    url(r'^bid/$', bid_view.tender_list, name='tender_feed'),
    url(r'^bidf/$', bid_view.tender_list_f, name='tender_feedF'),
    url(r'^bidc/$', bid_view.tender_list_c, name='tender_feedC'),
    url(r'^bid_historyf/$', bid_view.my_bids_f, name='bid_historyF'),
    url(r'^bid_history/$', bid_view.my_bids, name='bid_historyD'),
    url(r'^bid_historyc/$', bid_view.my_bids_c, name='bid_historyC'),
    path('bid<int:tender_id>', bid_view.index, name='bid_tender'),
    path('furn_bid<int:tender_id>', bid_view.furn_bid, name='furnBid'),
    path('const_bid<int:tender_id>', bid_view.const_bid, name='constBid'),
    path('bidview<int:bids_id>', bid_view.bid_update, name='deskBidUpdate'),
    path('constbidview<int:bids_id>', bid_view.const_bid_update, name='constBidUpdate'),
    path('furnbidview<int:bids_id>', bid_view.furn_bid_update, name='furnBidUpdate'),
    path('bidedit<int:bids_id>', bid_view.bid_edit, name='bid_edit'),
    path('constbidedit<int:bids_id>', bid_view.const_bid_edit, name='constBidEdit'),
    path('furnbidedit<int:bids_id>', bid_view.furn_bid_edit, name='furnBidEdit'),
    path('biddelete<int:pk>/', bid_view.del_bid, name='del_bid'),
    path('bidconstdelete<int:pk>/', bid_view.const_del_bid, name='constDelBid'),
    path('bidfurndelete<int:pk>/', bid_view.furn_del_bid, name='furnDelBid'),
    path('fullrepb', bid_view.aw_rep, name='awRepb'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
