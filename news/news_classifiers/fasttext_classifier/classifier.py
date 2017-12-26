# coding: utf8
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "news_configs.settings")
import django
django.setup()

import fasttext as ft
import jieba

# First download the dbpedia.train using https://github.com/facebookresearch/fastText/blob/master/classification-example.sh
# on test/ and move to the example directory
input_file = "/root/news-collector/news_classifiers/fasttext_classifier/news_fasttext_train.txt"

# Train the classifier
# classifier = ft.supervised("news_fasttext_train.txt",
#                            "news_fasttext.model", label_prefix="__label__")


# Predict some text
# (Example text is from dbpedia.train)


from news_web.models import News


class FasttextClassifier(object):

    @staticmethod
    def classify(**kvargs):
        classifier = ft.supervised("news_fasttext_train.txt",
                                   "news_fasttext.model", label_prefix="__label__")
        # classifier = ft.load_model(
        #     'news_fasttext.model.bin', label_prefix='__label__')
        news = News.objects.all()[:20]
        for new in news:
            text = new.n_abs
            seg_text = jieba.cut(text.replace("\t", " ").replace("\n", " "))
            outline = " ".join(seg_text)
            texts = [outline.encode("utf8")]
            labels = classifier.predict(texts)
            print text + ":" + labels[0][0]

if __name__ == '__main__':
    FasttextClassifier.classify()
