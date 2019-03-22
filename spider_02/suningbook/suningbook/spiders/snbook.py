# -*- coding: utf-8 -*-
import scrapy


class SnbookSpider(scrapy.Spider):
    name = 'snbook'
    allowed_domains = ['suning.com']
    start_urls = ['https://list.suning.com/1-502320-0.html']

    def parse(self, response):
        lis = response.xpath("//div[@id='filter-results']/ul/li")

        for li in lis:
            # price = li.xpath(".//div[@class='res-info']/p[@class='prive-tag']").extract_first()
            href = "http:"+li.xpath(".//div[@class='res-info']/p[@class='sell-point']/a/@href").extract_first()
            title = li.xpath(".//div[@class='res-info']/p[@class='sell-point']/a/text()").extract_first()
            item = dict({ "href": href,"title": title})
            yield scrapy.Request(href, callback=self.parse_details ,meta={"item": item})

    def parse_details(self, response):
        item = response.meta["item"]
        ul = response.xpath("//ul[contains(@class,'bk-publish')]")
        item["author"] = ul.xpath("./li[1]/text()").extract_first()
        item["publisher"] = ul.xpath("./li[2]/text()").extract_first()
        item["publish_date"] = ul.xpath("./li[3]/span[2]/text()").extract_first()
        print(response.xpath("//div[@id='priceDom']//span[@class='mainprice']"))
        item["price"] = response.xpath("//span[@class='mainprice']")
        yield item
        # print(item)



