# -*- coding: utf-8 -*-
import scrapy
import random
import threading
import time
import csv


class BossSpider(scrapy.Spider):
    name = 'boss'
    allowed_domains = ['zhipin.com']
    start_urls = ['https://www.zhipin.com/job_detail/?query=%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90&city=101270100&industry=&position=']
    base_url = 'http://www.zhipin.com/'
    base_city = '成都'

    def parse(self, response):

        lis = response.xpath("//div[@id='main']//ul/li")

        for li in lis:
            # price = li.xpath(".//div[@class='res-info']/p[@class='prive-tag']").extract_first()
            href = self.base_url+li.xpath("//div[@class='job-primary']//a/@href").extract_first()
            title = li.xpath("//div[@class='job-primary']//a/div[@class='job-title']/text()").extract_first()
            item = dict({ "boss链接": href,"职位名称": title})
            time.sleep(random.random() * 10)
            yield scrapy.Request(href, callback=self.parse_details ,meta={"item": item}, dont_filter=True)

        nexturl = self.base_url+response.xpath("//a[@ka='page-next']/@href").extract_first()
        while nexturl:
            print(nexturl)
            yield scrapy.Request(nexturl, callback=self.parse)

        # yield scrapy.Request(nexturl, callback=self.parse)

    def parse_details(self, response):

        item = response.meta["item"]
        item["城市"] = self.base_city
        item["薪资"] = response.xpath("//span[@class='salary']/text()").extract_first()
        item["学历要求"] = self.deal_em(response.xpath("//div[@class='job-banner']//p").extract())
        item["岗位福利"] = self.deal_with_dot(response.xpath("//div[@class='job-banner']//div[@class='job-tags']/span"))
        item["工作描述"] = self.deal_space_lst(response.xpath("//div[@class='detail-content']//div[@class='job-sec'][1]/div[@class='text']/text()").extract())

        # item["团队介绍"] = self.deal_with_dot(response.xpath(
        #     "//div[@class='detail-content']//div[@class='job-sec'][2]/div[@class='job-tags']/span"))
        item["公司福利"] = self.deal_with_dot(response.xpath("//div[@class='detail-content']//div[@class='job-sec'][2]/div[@class='job-tags']/span"))
        item["公司名称"] = response.xpath("//div[@class='sider-company']//a[@ka='job-detail-company_custompage']/text()").extract_first()
        item["融资情况"] = response.xpath(
            "//div[@class='sider-company']//i[@class='icon-stage']/../text()").extract_first()
        item["公司规模"] = response.xpath(
            "//div[@class='sider-company']//i[@class='icon-scale']/../text()").extract_first()
        item["公司行业"] = response.xpath(
            "//div[@class='sider-company']//a[@ka='job-detail-brandindustry']/text()").extract_first()
        item["公司地址"] = response.xpath("//div[@class='location-address']/text()").extract_first()



        # item["author"] = ul.xpath("./li[1]/text()").extract_first()
        # item["publisher"] = ul.xpath("./li[2]/text()").extract_first()
        # item["publish_date"] = ul.xpath("./li[3]/span[2]/text()").extract_first()
        # print(response.xpath("//div[@id='priceDom']//span[@class='mainprice']"))
        # item["price"] = response.xpath("//span[@class='mainprice']")

        yield item

    # spans 转成字逗号分隔字符串
    def deal_with_dot(self,spans):
        if spans:
            return  ",".join([span.xpath("./text()").extract_first() for span in spans])
        else:
            return ""

    def deal_space_lst(self,elements):
        if isinstance(elements,list):
            return " ".join(elements)
        else:
            return ""

    def deal_em(self,element):

        elements = element.split('<em class="dolt"></em>')

        return elements