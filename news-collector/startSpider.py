#!/usr/bin/env python
import os


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "news_collector.settings")
    from news_spiders.base.testSpider import TestSpider
    TestSpider().spiderNews()
