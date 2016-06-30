# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DuplicatesTitlePipeline(object):
    __titles = []

    def process_item(self, item, spider):
        if not item['title'] in self.__titles:
            self.__titles.append(item['title'])
            return item


class SaveModelPipeline(object):

    def process_item(self, item, spider):
        item.saveModel()
        return item
