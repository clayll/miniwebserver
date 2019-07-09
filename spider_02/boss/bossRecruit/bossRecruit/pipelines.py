# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import csv
import json


class BossrecruitPipeline(object):
    def process_item(self, item, spider):

        # with open("ceshi.json",mode="a",encoding="utf-8") as f:

        # jsonitem = json.dumps(item,ensure_ascii=False,indent=2)
        # f.write(jsonitem+",")
        f = open(item["城市"]+".csv", mode="a", encoding="utf-8")
        writer =csv.writer(f)
        keys = list(item.keys())
        # writer.writerow(keys)  # 将属性列表写入csv中
        # flag = False
        #  else:
        #     # 读取json数据的每一行，将values数据一次一行的写入csv中
        writer.writerow(list(item.values()))

        return item




