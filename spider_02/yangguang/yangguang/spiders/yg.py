# -*- coding: utf-8 -*-
import scrapy


class YgSpider(scrapy.Spider):
    name = 'yg'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4&page=0']

    def parse(self, response):
        tds = response.xpath("//div[@class='pagecenter']//tr")[1:-1]
        print(tds)
        for t in tds:
            href = t.xpath(".//a[2]/@href").extract_first()
            title = t.xpath(".//a[2]/text()").extract_first()
            item = dict({"title":title,"href":href})
            scrapy.Request(href , callback=self.parseDetails)

        yield

    def parseDetails(self, response):
        print(response.Meta["item"])
        pass

