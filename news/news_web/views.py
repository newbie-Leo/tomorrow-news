# coding: utf8
import json
import requests
from django.shortcuts import render_to_response
from django.template.response import TemplateResponse
from django.http import HttpResponse
from news_web.models import News
from util import transform_img, transform_title
# Create your views here.


def index(request):
    # 获取有图头条
    main_news = News.get_main_news(request)
    main = json.dumps([
        {
            'title': transform_title(i.title),
            'link': '/news?id=%s' % i.id,
            'img': transform_img(
                json.loads(
                    i.imageurls
                )[0]['url']),
            'desc': u'【%s】%s' % (i.site, i.n_abs)
        }

        for i in main_news
    ])

    main_pic_news = News.get_pic_main_news(request)
    main_pic_news = json.dumps([
        {
            'title': transform_title(i.title),
            'link': '/news?id=%s' % i.id,
            'img': transform_img(
                json.loads(
                    i.imageurls
                )[0]['url']),
        }

        for i in main_pic_news
    ])

    # 获取无图头条
    no_pic_news = News.get_no_pic_main_news(request)
    no_pic_main = json.dumps([
        {
            'title': transform_title(i.title),
            'link': '/news?id=%s' % i.id,
            'date': i.site
        }

        for i in no_pic_news
    ])

    data = {'main': main,
            'main_pic_news': main_pic_news,
            'no_pic_main': no_pic_main,
            }
    return render_to_response('index.html', data)


def news_list(request):
    if not request.GET.get('callback'):
        data = {"b_type":
                request.GET.get("b_type", "")}
        return render_to_response('newslist.html', data)
    callback = request.GET.get('callback')
    start = int(request.GET.get('start'))
    count = int(request.GET.get('count'))

    news, total, start = News.get_news_list(request, start=start, count=count)

    news = [
        {
            'title': transform_title(i.title),
            'link': '/news?id=%s' % i.id,
            'desc': i.n_abs,
            'id': i.id
        }

        for i in news
    ]

    dic = {'count': count, 'start': start, 'total': total, 'events': news}

    js = ";%s(%s)" % (callback, json.dumps(dic))
    return HttpResponse(js)


def news(request):
    newsid = request.GET.get('id')
    new = News.objects.get(id=newsid)
    return TemplateResponse(request, "new.html", {"new": new})


def img(request):
    url = request.GET.get('url')
    headers = {'Referer': url}
    response = requests.get(url, headers=headers)

    res = HttpResponse(response.content)
    res['Content-Type'] = 'image/jpeg'
    return res
