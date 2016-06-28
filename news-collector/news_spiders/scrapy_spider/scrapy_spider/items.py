# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapySpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
    nid = scrapy.Field()
    site = scrapy.Field()
    ts = scrapy.Field()
    b_type = scrapy.Field()
    imageurls = scrapy.Field()
    n_abs = scrapy.Field()
    n_date = scrapy.Field()
