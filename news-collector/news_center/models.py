# coding: utf8
from django.db import models
from datetime import datetime
from util import translateImg
# Create your models here.


class News(models.Model):
    title = models.CharField(u'标题', max_length=100)
    url = models.CharField(u'来源地址', max_length=1024)
    nid = models.CharField(u'nid', max_length=30)
    site = models.CharField(u'来源媒体', max_length=30, null=True)
    ts = models.DateField(u'发布时间', null=True)
    b_type = models.CharField(u'类型', max_length=30, null=True)
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
    def getMainNews(cls):
        # TODO 筛选头条新闻（有图）
        news = cls.objects.filter(
            n_date=datetime.today()).exclude(imageurls='[]')[0:4]
        return news

    @classmethod
    def getPicMainNews(cls):
        # TODO 筛选头条新闻（有图）
        news = cls.objects.filter(
            n_date=datetime.today()).exclude(imageurls='[]')[4:8]
        return news

    @classmethod
    def getNoPicMainNews(cls):
        # TODO 筛选头条新闻（无图）
        news = cls.objects.filter(n_date=datetime.today(), imageurls='[]')[0:4]
        return news

    @classmethod
    def getNewsList(cls, start=0, count=10, type=None):
        news = cls.objects.filter(n_date=datetime.today())[
            start: start + count]
        count = cls.objects.all().count()
        return news, count


class NewsContent(models.Model):
    news = models.OneToOneField(News, related_name='news_content')
    content = models.TextField(u'内容', null=True)
    content_img = models.CharField(u'内容图片', max_length=512, null=True)
    content_movie = models.CharField(u'视频', max_length=512, null=True)

    @property
    def jump_img(self):
        return translateImg(self.content_img)

    class Meta:
        db_table = 'news_content'
        verbose_name_plural = u"新闻内容"
        verbose_name = u"新闻内容"
