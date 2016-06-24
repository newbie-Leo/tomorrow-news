from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'news_collector.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^index$', 'news_center.views.index', name='index'),
                       url(r'^img$', 'news_center.views.img', name='img'),
                       url(r'^newslist$', 'news_center.views.newsList', name='newslist'),
                       )
