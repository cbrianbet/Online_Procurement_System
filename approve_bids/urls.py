from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('list<int:bid_id>', views.bid_for_tender_list, name='accept_list'),
    path('listfurn<int:bid_id>', views.bid_furn_tender_list, name='acceptFurn'),
    path('listconst<int:tender_id>', views.bid_const_tender_list, name='acceptConst'),
    path('approve<int:b_id>', views.accept_bid, name='approve_bid'),
    path('approveconst<int:b_id>', views.accept_const_bid, name='approveConstBid'),
    path('approvefurn<int:b_id>', views.accept_furn_bid, name='approveFurnBid'),
    path('info<int:bid>', views.bid_info, name='user_info'),
    path('desk_userinfo<int:bid>', views.bid_info, name='deskUserInfo'),
    path('furn_userinfo<int:bid>', views.bid_info, name='furnUserInfo'),
    path('bidrej<int:pk>/', views.del_bid, name='desRejectBid'),
    path('bidconstrej<int:pk>/', views.const_del_bid, name='constRejectBid'),
    path('bidfurnrej<int:pk>/', views.furn_del_bid, name='furnRejectBid'),
    path('afurnview<int:bid>/', views.furn_view_bid, name='awFurnView'),
    path('adeskview<int:bid>/', views.view_bid, name='awDeskView'),
    path('aconstview<int:bid>/', views.const_view_bid, name='awConstView'),
    # path('auto_award<int:tender_id>/', views.auto_award, name='autoAward'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
