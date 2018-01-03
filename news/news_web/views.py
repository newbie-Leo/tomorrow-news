# coding: utf8
import json
import requests
from django.shortcuts import render_to_response
from django.template.response import TemplateResponse
from django.http import HttpResponse
from news_web.models import News
from util import news_query_set_to_json, new_to_dict
# Create your views here.


def index(request):
    # 获取有图头条
    main_news = News.get_main_news(request)
    main = news_query_set_to_json(main_news)

    main_pic_news = News.get_pic_main_news(request)
    main_pic_news = news_query_set_to_json(main_pic_news)

    # 获取无图头条
    no_pic_news = News.get_no_pic_main_news(request)
    no_pic_main = news_query_set_to_json(no_pic_news)

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
    news, total, start = News.get_news_list(request, start=start, size=count)
    news = [new_to_dict(i) for i in news]
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
