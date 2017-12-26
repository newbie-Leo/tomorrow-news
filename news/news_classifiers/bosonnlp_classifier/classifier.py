# coding: utf8
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "news_configs.settings")
import django
django.setup()

from bs4 import BeautifulSoup
from django.conf import settings
from bosonnlp import BosonNLP
from news_web.models import News


class BosonNLPClassifier(object):
    token = settings.BOSON_TOKEN
    nlp = BosonNLP(token)

    @staticmethod
    def classify_one(new):
        try:
            # content_text = BeautifulSoup(new.news_content.content).getText()
            btype = BosonNLPClassifier.nlp.classify(new.n_abs)[0]
            new.b_type = btype
            new.save()
        except:
            pass

    @staticmethod
    def classify(**kvargs):
        news = News.objects.filter(b_type=None)
        for new in news:
            BosonNLPClassifier.classify_one(new)


if __name__ == '__main__':
    BosonNLPClassifier.classify()
