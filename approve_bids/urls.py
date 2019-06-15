from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('list<int:bid_id>', views.bid_for_tender_list, name='accept_list'),
    path('approve<int:b_id>', views.accept_bid, name='approve_bid'),
    path('info<int:bid>', views.bid_info, name='bid_info'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)