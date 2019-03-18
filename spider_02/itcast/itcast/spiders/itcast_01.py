# -*- coding: utf-8 -*-
import scrapy


class Itcast01Spider(scrapy.Spider):
    name = 'itcast_01'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):

        tearchaers = response.xpath("//div[@class='tea_con']//div[@class='li_txt']")
        for t in tearchaers:
            name = t.xpath("./h3/text()").extract_first()
            position = t.xpath("./h4/text()").extract_first()
            profile = t.xpath("./p/text()").extract_first()
            item = {"name" : name,"position":position,"profile" : None}
            print(item)
            yield item

