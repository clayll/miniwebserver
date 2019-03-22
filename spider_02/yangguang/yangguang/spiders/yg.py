# -*- coding: utf-8 -*-
import scrapy
from  yangguang.items import YangguangItem


class YgSpider(scrapy.Spider):
    name = 'yg'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4&page=0']

    def parse(self, response):
        tds = response.xpath("//div[@class='pagecenter']//tr")[1:-1]
        for t in tds:
            item = YangguangItem()
            item["href"] = t.xpath(".//a[2]/@href").extract_first()
            item["title"] = t.xpath(".//a[2]/text()").extract_first()

            yield scrapy.Request(item["href"] , callback=self.parseDetails,meta={"item":item})

        nexturl =response.xpath("//div[@class='pagination']/a[text()='>']/@href").extract_first()
        while nexturl:
            yield scrapy.Request(nexturl, callback=self.parse)

    def parseDetails(self, response):
        td = response.xpath("//td[@class='txt16_3']")
        item = response.meta["item"]
        item["content"] = td.xpath(".//text()").extract()
        item["img"] = td.xpath(".//img/@src").extract()
        yield item

