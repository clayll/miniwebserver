# -*- coding: utf-8 -*-
import json

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ItcastPipeline(object):
    def process_item(self, item, spider):
        with open("itcast_teacher.txt","a",encoding="utf-8") as f:
            f.write(json.dumps(item, indent=2, ensure_ascii=False))

