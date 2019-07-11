from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls import url, include
from core import views as core_views
from django.conf.urls.static import static
from reports.views import *

urlpatterns = [

    path('admin/', admin.site.urls),
    path('home/', include('home.urls')),
    url(r'^', include('login.urls'), name='login'),
    url(r'^signup/$', core_views.signup, name='signup'),
    path('create/', include('create_tender.urls')),
    path('buyer/', include('approve_bids.urls')),
    path('rep<int:tender_id>', GeneratePdf.as_view(), name='rep'),
    path('frep<int:tender_id>', GenerateFurnPdf.as_view(), name='frep'),
    path('crep<int:tender_id>', GenerateConstPdf.as_view(), name='crep'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
