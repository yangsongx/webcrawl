# -*- coding: utf-8 -*-

import pymongo

from scrapy.exceptions import DropItem

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DoubanPipeline(object):

    def __init__(self):
        #usually prepare the DB
        conn = pymongo.MongoClient("172.20.20.239")
        self.db = conn["douban"]

    def process_item(self, item, spider):
        # Here simple insert
        self.db.data.insert(dict(item))
        return item
