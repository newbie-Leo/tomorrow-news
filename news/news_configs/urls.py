from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import RedirectView
from news_web.views import *
from rest_framework import routers
from restapi import views

router = routers.DefaultRouter()
router.register(r'restnews', views.NewsViewSet)
admin.autodiscover()

urlpatterns = (
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index$', index, name='index'),
    url(r'^img$', img, name='img'),
    url(r'^newslist$', news_list, name='newslist'),
    url(r'^news$', news, name='news'),
    url(r'^rest/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^$', RedirectView.as_view(pattern_name='index')),
)
