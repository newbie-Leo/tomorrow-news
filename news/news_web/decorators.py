# coding: utf8


def dynamic_news_decoder(func):

    def w(cls, request, last_readed=0, **kv):
        last_readed = request.session.get("last_readed", 0)
        news = func(cls, request, last_readed, **kv)
        length = len(news)
        if length < 8:
            request.session['last_readed'] = 0
            return func(cls, request, last_readed=0, **kv)
        new = news[len(news) - 1]
        request.session['last_readed'] = new.id
        return news
    return w
