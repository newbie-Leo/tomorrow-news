from datetime import datetime
import json
from django import template
from django.template.loader import get_template
from django.db.models import Count
from django.urls import reverse
from news_center.models import News, NEWS_TYPE_CHOICES

register = template.Library()


@register.simple_tag
def menu_list():
    menus = News.get_menus()
    menus_data = [{"type": i[0], "name": dict(NEWS_TYPE_CHOICES)[i[0]]}
                  for i in menus]
    data = {"menus": menus_data}
    tpl = get_template("menus.html")
    return tpl.render(data)


@register.simple_tag
def menu_json():
    menus = News.get_menus()
    menus_data = [{"link": "%s?b_type=%s" % (reverse("newslist"), i[0]),
                   "title": dict(NEWS_TYPE_CHOICES)[i[0]]}
                  for i in menus]

    return json.dumps(menus_data)
