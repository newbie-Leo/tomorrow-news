# coding:utf8
from datetime import datetime
import requests
from baseSpider import BaseSpider
from news_center.models import News
import json


class TestSpider(BaseSpider):

    def spiderNews(self, **kvargs):
        url = "http://180.149.132.136/sn/api/searchnews"
        for i in range(10):
            self.__spiderOneNews(url, i)

    def __spiderOneNews(self, url, pn):
        data = {}
        data['pn'] = pn
        data['word'] = self.tomorrowStr.encode("utf8")
        js = requests.get(url, data).json()
        news = js['data']['news']

        for i in news:
            print i
            title = i['title']
            url = i['url']
            nid = i['nid']
            site = i['site']
            ts = datetime.fromtimestamp(float(i['ts']) / 1000)
            imageurls = json.dumps(i['imageurls'])
            n_abs = i['abs']
            n_date = datetime.now()
            new = News(title=title, url=url, nid=nid, site=site,
                       ts=ts, imageurls=imageurls, n_abs=n_abs,
                       n_date=n_date)
            new.save()
