from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from core import views as core_views
from tender_feed import views as feed_views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('home/', include('home.urls')),
    url(r'^', include('login.urls'), name='login'),
    url(r'^signup/$', core_views.signup, name='signup'),
    url(r'^feed/$', feed_views.feed, name='feed'),
    path('create/', include('create_tender.urls')),
]
