# coding: utf8
from datetime import datetime
from datetime import timedelta


class BaseSpider(object):
    '''
    爬虫基类，所有爬虫须继承此类并实现方法
    '''
    @property
    def tomorrowStr(self):
        today = datetime.today()
        tomorrow = today + timedelta(days=1)
        month = tomorrow.month
        day = tomorrow.day
        return u'%s月%s日' % (month, day)

    def spiderNews(self, **kvargs):
        '''
        爬取新闻
        '''
        raise NotImplementedError(
            'subclasses of BaseSpider must provide a spiderNews method')
