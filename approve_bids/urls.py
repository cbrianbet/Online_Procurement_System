from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('list<int:bid_id>', views.bid_for_tender_list, name='accept_list'),
    path('approve<int:b_id>', views.accept_bid, name='approve_bid'),
    path('info<int:bid>', views.bid_info, name='bid_info'),

]
