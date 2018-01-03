# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from goose import Goose
from goose.text import StopWordsChinese
from lxml import etree
from scrapy.exceptions import DropItem
from news_web.models import NewsContent, NewsSite
from news_web.util import get_tomorrow


class DuplicatesTitlePipeline(object):
    __titles = []

    def process_item(self, item, spider):
        if not item['title'] in self.__titles:
            self.__titles.append(item['title'])
            return item
        else:
            raise DropItem(u"标题重复 %s" % item)


class PublishDatePipeline(object):

    def process_item(self, item, spider):
        ts = item['ts']
        tomorrow = get_tomorrow()
        passed = tomorrow - ts
        if passed.days >= 300:
            raise DropItem(u"新闻不符 %s" % item)
        else:
            return item


class SaveModelPipeline(object):

    def process_item(self, item, spider):
        if item:
            media_name = item['site']
            item_media, _ = NewsSite.objects.get_or_create(
                site_name=media_name)
            item['b_type'] = item_media.site_type
            dbitem = item.save_model()
            return dbitem


class GetContentPipeline(object):
    goose = Goose({'stopwords_class': StopWordsChinese})

    def process_item(self, item, spider):
        if item:
            url = item.url
            new_content = NewsContent()
            new_content.news = item
            article = GetContentPipeline.goose.extract(url=url)

            if (not article) or not (article.top_node):
                item.delete()
                raise DropItem(u"无法获取内容 %s" % item)
            text = article.top_node.text_content()
            if not text:
                item.delete()
                raise DropItem(u"无法获取内容 %s" % item)

            content = etree.tostring(article.top_node)
            text = BeautifulSoup(content).getText()
            if len(text) < 100:
                item.delete()
                raise DropItem(u"获取内容太短 %s" % item)
            new_content.content = content
            try:
                img = article.top_image.src
                new_content.content_img = img
                movie = article.movies[0].src
                new_content.movie = movie
            except:
                pass
            new_content.save()
            return item
