# -*- coding: utf-8 -*-
import scrapy,json

class JdforbookSpider(scrapy.Spider):
    name = 'jdforbook'

    allowed_domains = ['book.jd.com','list.jd.com', 'p.3.cn']
    start_urls = ['https://book.jd.com/booksort.html/']
    baseUrl = "https:"

    def parse(self, response):
        item = dict()
        ems = response.xpath("//div[@class='mc']/dl/dd[1]/em")

        for em in ems:
            item["category_href"] = self.baseUrl+em.xpath("./a/@href").extract_first()
            item["category"] = em.xpath("./a/text()").extract_first()

            yield scrapy.Request(item["category_href"],callback=self.parse_list, meta={"item":item})


    def parse_list(self,response:scrapy.http.response.Response):
        item = response.meta["item"]
        lis = response.xpath("//div[@id='plist']/ul/li[@class='gl-item']")

        for li in lis:
            item["title"] = li.xpath("//div[@class='p-name']/a/em/text()").extract_first()
            item["title"] = str.replace(item["title"],r"\n","").strip()
            item["skuId"] = li.xpath("//div[contains(@class,'j-sku-item')]/@data-sku").extract_first()
            item["href"] = self.baseUrl+li.xpath("//div[@class='p-name']/a/@href").extract_first()
            item["img"] = self.baseUrl+li.xpath("//div[@class='p-img']/a/img/@src").extract_first()

            if item["skuId"]:
                url = "https://p.3.cn/prices/mgets?skuIds=J_"+item["skuId"]
                yield scrapy.Request(url, callback=self.parse_price, meta={"item": item})
            else:
                print(item)
                yield item

    def parse_price(self,response:scrapy.http.response.Response):
        item = response.meta["item"]
        priceObj = json.loads(response.body.decode("utf-8"))
        item["price"] = priceObj[0]["op"]
        yield item
        print(item)

