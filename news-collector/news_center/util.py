# coding:utf8
import urllib
import json
from datetime import datetime, timedelta


def translateImg(imgurl):
    url = '/img?url=%s' % urllib.quote(imgurl)
    return url


def translateTitle(title):
    today = datetime.today()
    tomorrow = today + timedelta(days=1)
    month = tomorrow.month
    day = tomorrow.day
    tomorrow = u'%s月%s日' % (month, day)
    return title.replace(tomorrow, u"明天")


def newsQuerySetToJson(news):
    news_json = json.dumps([
        {
            'title': translateTitle(i.title),
            'link': i.url,
            'img': translateImg(
                json.loads(
                    i.imageurls
                )[0]['url'] if not i.imageurls == '[]' else ''),
            'desc': i.n_abs,
            'date': i.ts.strftime('%Y-%m-%d')
        }

        for i in news
    ])

    return news_json
