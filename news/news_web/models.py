# coding: utf8
from django.db import models
from django.db.models import Count
from datetime import datetime
from util import transform_img, get_tomorrow
from decorators import dynamic_news_decoder
# Create your models here.

NEWS_TYPE_CHOICES = (
    (0,  u'体育'),
    (1,  u'教育'),
    (2,  u'财经'),
    (3,  u'社会'),
    (4,  u'娱乐'),
    (5,  u'军事'),
    (6,  u'国内'),
    (7,  u'科技'),
    (8,  u'互联网'),
    (9,  u'房产'),
    (10, u'国际'),
    (11, u'女人'),
    (12, u'汽车'),
    (13, u'游戏'),
)


class News(models.Model):
    title = models.CharField(u'标题', max_length=100)
    url = models.CharField(u'来源地址', max_length=1024)
    nid = models.CharField(u'nid', max_length=30)
    site = models.CharField(u'来源媒体', max_length=30, null=True)
    ts = models.DateField(u'发布时间', null=True)
    b_type = models.SmallIntegerField(u'类型',
                                      choices=NEWS_TYPE_CHOICES, null=True)
    imageurls = models.CharField(u'图片', max_length=1024, null=True)
    n_abs = models.CharField(u'原标题', max_length=100, null=True)
    n_date = models.DateField(u'日期', db_index=True)

    def __unicode__(self):
        return self.title

    class Meta:
        db_table = 'news'
        verbose_name_plural = u"新闻"
        verbose_name = u"新闻"

    @classmethod
    @dynamic_news_decoder
    def get_main_news(cls, request, last_readed=0):
        # TODO 筛选头条新闻（有图）
        news = cls.objects.filter(
            n_date=get_tomorrow(),
            id__gt=last_readed).exclude(imageurls='[]')[0:9]

        return news

    @classmethod
    def get_pic_main_news(cls, request):
        last_readed = request.session.get("last_readed", 0)

        # TODO 筛选头条新闻（有图）
        news = cls.objects.filter(
            n_date=get_tomorrow(), id__gte=last_readed).exclude(imageurls='[]')[9:13]

        print news
        return news

    @classmethod
    @dynamic_news_decoder
    def get_no_pic_main_news(cls, request, last_readed=0):
        # TODO 筛选头条新闻（无图）
        news = cls.objects.filter(n_date=get_tomorrow(),
                                  id__gt=last_readed, imageurls='[]')[0:9]
        return news

    @classmethod
    def get_news_list(cls, request, start=0, size=10, type=None):
        b_type = request.GET.get("b_type")
        if start == 0:
            start = request.session.get(
                b_type + "last_start", 0)
        query = {"n_date": get_tomorrow()}
        if b_type:
            query["b_type"] = int(b_type)

        news = cls.objects.filter(**query)[
            start: start + size]
        count = news.count()
        # print news
        # print query
        request.session[b_type + "last_start"] = start
        return news, count, start

    @classmethod
    def get_menus(cls):
        menus = cls.objects.filter(
            n_date=get_tomorrow()).exclude(b_type=None).values_list(
            'b_type').annotate(counts=Count('id')).filter(counts__gt=0)

        return menus


class NewsContent(models.Model):
    news = models.OneToOneField(News, related_name='news_content')
    content = models.TextField(u'内容', null=True)
    content_img = models.CharField(u'内容图片', max_length=512, null=True)
    content_movie = models.CharField(u'视频', max_length=512, null=True)

    @property
    def jump_img(self):
        return transform_img(self.content_img)

    class Meta:
        db_table = 'news_content'
        verbose_name_plural = u"新闻内容"
        verbose_name = u"新闻内容"


class NewsSite(models.Model):

    site_name = models.CharField(u'媒体名称', max_length=30, null=True)
    site_type = models.SmallIntegerField(
        u'媒体类型', null=True, choices=NEWS_TYPE_CHOICES)

    class Meta:
        db_table = 'media_site'
        verbose_name_plural = u"媒体"
        verbose_name = u"媒体"
