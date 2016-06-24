# coding: utf8
import json
import requests
from django.shortcuts import render_to_response
from django.http import HttpResponse
from news_center.models import News
from util import translateImg, translateTitle
# Create your views here.


def index(request):
    # 获取有图头条
    main_news = News.getMainNews()
    main = json.dumps([
        {
            'title': translateTitle(i.title),
            'link': i.url,
            'img': translateImg(
                json.loads(
                    i.imageurls
                )[0]['url']),
            'desc': i.n_abs
        }

        for i in main_news
    ])

    main_pic_news = News.getPicMainNews()
    main_pic_news = json.dumps([
        {
            'title': translateTitle(i.title),
            'link': i.url,
            'img': translateImg(
                json.loads(
                    i.imageurls
                )[0]['url']),
        }

        for i in main_pic_news
    ])

    # 获取无图头条
    no_pic_news = News.getNoPicMainNews()
    no_pic_main = json.dumps([
        {
            'title': translateTitle(i.title),
            'link': i.url,
            'date': i.ts.strftime('%Y-%m-%d')
        }

        for i in no_pic_news
    ])

    data = {'main': main, 'main_pic_news': main_pic_news,
            'no_pic_main': no_pic_main}
    return render_to_response('index.html', data)


def newsList(request):
    if not request.GET.get('callback'):
        return render_to_response('newslist.html')
    callback = request.GET.get('callback')
    start = int(request.GET.get('start'))
    count = int(request.GET.get('count'))

    news, total = News.getNewsList(start=start, count=count)

    news = [
        {
            'title': translateTitle(i.title),
            'link': i.url,
            'desc': i.n_abs,
            'id': i.id
        }

        for i in news
    ]

    dic = {'count': count, 'start': start, 'total': total, 'events': news}

    js = ";%s(%s)" % (callback, json.dumps(dic))
    return HttpResponse(js)


def img(request):
    url = request.GET.get('url')
    headers = {'Referer': 'http://www.baidu.com/'}
    response = requests.get(url, headers=headers)

    res = HttpResponse(response.content)
    res['Content-Type'] = 'image/jpeg'
    return res
