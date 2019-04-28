# -*- coding: utf-8 -*-
import scrapy
from dyttSpider.items import DyttspiderItem
import re

# 执行命令 scrapy crawl dyttSpider_01 -o test.csv
class Dyttspider01Spider(scrapy.Spider):
    name = 'dyttSpider_01'
    allowed_domains = ['www.ttmeiju.me']
    start_urls = ['http://www.ttmeiju.me/article.html']
    baseUrl = "http://www.ttmeiju.me"

    def parse(self, response):
        list = response.xpath("//div[@class='contentbox']/ul[@class='news-list']/li")
        for li in list:
            item = DyttspiderItem()
            item["name"] = li.xpath("div[@class='newstit']/a/text()").extract_first()
            item["introduction"] = li.xpath("div[@class='contents']/div[@class='newsinfo']/p/text()").extract_first()
            item["comeFrom"] = li.xpath("div[@class='newstit']/label/text()").extract_first()
            item["imghref"] = li.xpath("div[@class='contents']/div[@class='cover']/a/img/@src").extract_first()
            item["detailsUrl"] =  Dyttspider01Spider.baseUrl+li.xpath("div[@class='contents']/div[@class='newsinfo']/p/a/@href").extract_first() if li.xpath("div[@class='contents']/div[@class='newsinfo']/p/a/@href")  else ""
            item["comments"] = re.match("[0-9]+", li.xpath("div[@class='views']/child::text()[2]").extract_first()).group(0)

            yield item
        scrapy.selector.unified.SelectorList
        #获取URL

        nextPage = response.xpath("//ul[@class='pagination']/li[@class='active']/following-sibling::li[2]/a/@href").extract_first()
        print("nextPage:",nextPage)
        if nextPage is not None:
            nextPage = "http://www.ttmeiju.me"+nextPage
            yield scrapy.Request(nextPage, callback=self.parse)