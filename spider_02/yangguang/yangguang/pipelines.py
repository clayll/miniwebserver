# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo.mongo_client import MongoClient

class YangguangPipeline(object):

    def open_spider(self, spider):
        dbcon =  MongoClient(host=spider.settings.get("DB_HOST", spider.settings.get("DB_PORT")))
        db = dbcon[spider.settings.get("DB_NAME")]
        self.connetions = db[spider.settings.get("DB_CONNECTIONS")]
    # def __init__(self):
    #     dbcon =  MongoClient("localhost", "27017")
    #     db = dbcon[spider.settings.get("yangguang")]
    #     self.connetions = db["test1"]


    def process_item(self, item, spider):
        self.connetions.insert(dict(item))

