# coding: utf8
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "news_collector.settings")
import django
django.setup()


from django.conf import settings
from bosonnlp import BosonNLP
from news_center.models import News


class BosonNLPClassifier(object):
    token = settings.BOSON_TOKEN
    nlp = BosonNLP(token)

    @staticmethod
    def classifyOne(new):
        try:
            btype = BosonNLPClassifier.nlp.classify(new.n_abs)[0]
            new.b_type = btype
            new.save()
        except:
            pass

    @staticmethod
    def classify(**kvargs):
        news = News.objects.filter(b_type=None)
        for new in news:
            BosonNLPClassifier.classifyOne(new)


if __name__ == '__main__':
    BosonNLPClassifier.classify()
