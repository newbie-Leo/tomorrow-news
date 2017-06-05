# coding: utf8
import json
from datetime import datetime, timedelta
import scrapy
from scrapy_spider.items import ScrapySpiderItem


class NewsSpider(scrapy.spiders.Spider):
    page = 1
    name = "news"
    # 定义spider名字的字符串(string)。spider的名字定义了Scrapy如何定位(并初始化)spider，
    # 所以其必须是唯一的。
    # 不过您可以生成多个相同的spider实例(instance)，这没有任何限制。
    # name是spider最重要的属性，而且是必须的。
    # 如果该spider爬取单个网站(single domain)，一个常见的做法是以该网站(domain)(加或不加 后缀)来命名
    # spider。 例如，如果spider爬取 mywebsite.com ，该spider通常会被命名为

    start_urls = [
        "http://api.baiyue.baidu.com/sn/api/searchnews",
    ]

    items = []
    # URL列表。当没有制定特定的URL时，spider将从该列表中开始进行爬取。
    # 因此，第一个被获取到的页面的URL将是该列表之一。
    # 后续的URL将会从获取到的数据中提取。

    # def start_requests():
    #     '''
    #     该方法必须返回一个可迭代对象(iterable)。该对象包含了spider用于爬取的第一个Request。
    #     当spider启动爬取并且未制定URL时，该方法被调用。
    #     当指定了URL时，make_requests_from_url() 将被调用来创建Request对象。
    #     该方法仅仅会被Scrapy调用一次，因此您可以将其实现为生成器。
    #     该方法的默认实现是使用 start_urls 的url生成Request。
    #     '''
    #     pass

    def make_requests_from_url(self, url):
        return scrapy.FormRequest(url,
                                  formdata=self.__make_params(),
                                  method='GET')

    @property
    def tomorrowStr(self):
        today = datetime.today()
        tomorrow = today + timedelta(days=1)
        month = tomorrow.month
        day = tomorrow.day
        return u'%s月%s日' % (month, day)

    def __make_params(self):
        data = {}
        data['pn'] = str(self.page)
        data['word'] = self.tomorrowStr.encode("utf8")
        return data

    def parse(self, response):
        body = json.loads(response.body)
        hasmore = body['data']['hasmore']
        news = body['data']['news']
        for i in news:
            item = self.__make_item(i)
            self.items.append(item)

        if(self.page < 50 and hasmore):
            self.page = self.page + 1
            yield self.make_requests_from_url(
                self.start_urls[0])
        else:
            for i in self.items:
                yield i

    def __make_item(self, i):
        title = i['title']
        url = i['url']
        nid = i['nid']
        site = i['site']
        ts = datetime.fromtimestamp(float(i['ts']) / 1000)
        imageurls = json.dumps(i['imageurls'])
        n_abs = i['abs']
        n_date = datetime.now()

        item = ScrapySpiderItem(title=title, url=url, nid=nid, site=site,
                                ts=ts, imageurls=imageurls, n_abs=n_abs,
                                n_date=n_date)
        return item
