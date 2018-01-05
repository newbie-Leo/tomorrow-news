# coding:utf8
import urllib
import json
from datetime import datetime, timedelta


def transform_img(imgurl):
    url = '/img?url=%s' % urllib.quote(imgurl)
    return url


def transform_title(title):
    today = datetime.today()
    tomorrow = today + timedelta(days=1)
    year = tomorrow.year
    month = tomorrow.month
    day = tomorrow.day
    tomorrow_normal = u'%s月%s日' % (month, day)
    tomorrow_abnormal = tomorrow.strftime("%m月%d日").decode("utf8")
    yaer_normal = u"%s年" % year
    yaer_abnormal = u"明年"

    tm_index = None
    if tomorrow_abnormal in title:
        tm_index = title.find(tomorrow_abnormal)
        title = title.replace(tomorrow_abnormal, u"明天")
    else:
        tm_index = title.find(tomorrow_normal)
        title = title.replace(tomorrow_normal, u"明天")
    if not tm_index is None:
        if title[tm_index - 5: tm_index] == yaer_normal:
            title = title.replace(yaer_normal, u"")
        elif title[tm_index - 2: tm_index] == yaer_abnormal:
            title = title.replace(yaer_abnormal, u"")
    return title


def get_tomorrow():
    today = datetime.today()
    tomorrow = today + timedelta(days=1)
    return tomorrow


def new_to_dict(new):
    new_dict = {
        'title': transform_title(new.title),
        'link': '/news?id=%s' % new.id,
        'img': transform_img(
            json.loads(
                new.imageurls)[0]['url']
            if not new.imageurls == '[]' else ''),
        'desc': new.n_abs,
        # 'date': new.ts.strftime('%Y-%m-%d')
    }
    return new_dict


def news_query_set_to_json(news):
    news_dict = [new_to_dict(new) for new in news]
    return json.dumps(news_dict)
