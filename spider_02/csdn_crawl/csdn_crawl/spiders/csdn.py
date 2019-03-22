# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class CsdnSpider(CrawlSpider):
    name = 'csdn'
    # allowed_domains = ['csdn.cn']
    # start_urls = ['http://csdn.cn/']
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4&page=']

    # 每一页的匹配规则
    pagelink = LinkExtractor(allow=('type=4'))
    rules = (
        Rule(pagelink, callback='parse_item',process_links = "deal_links", follow=False),
    )

    def deal_links(self, links):
        for link in links:
            link.url = link.url.replace("?", "&").replace("Type&", "Type?")
            print(link.url)

        return links

    def parse_item(self, response):
        item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        print()
        return item
