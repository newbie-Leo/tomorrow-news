from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import RedirectView
from news_center.views import *

admin.autodiscover()
urlpatterns = (
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index$', index, name='index'),
    url(r'^img$', img, name='img'),
    url(r'^newslist$', newsList, name='newslist'),
    url(r'^news$', news, name='news'),
    url(r'^$', RedirectView.as_view(pattern_name='index')),
)
