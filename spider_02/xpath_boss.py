from lxml import etree
from io import StringIO, BytesIO

import requests,json,time
import random
import csv
from pprint import pprint

class baidu_tieba_jijian():

    def __init__(self,kw):
        self.tiebaName = kw
        self.headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0"}
        self.url_list = []
        self.base_city = kw

    def init_allUrl(self):
        self.start_url = "https://www.zhipin.com/job_detail/?query=%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90&city=101270100&industry=&position="
        self.baseurl ='http://www.zhipin.com/'
        # "https://tieba.baidu.com/mo/q---E43010237FA469B37C96EDE1EAD664A9%3AFG%3D1-sz%40320_240%2C-1-3-0--2--wapp_1551576146607_550/"

        self.url_list.append(self.start_url)

    def  parse_url(self,url):

        response = requests.get(url, headers=self.headers)
        return response.text

    def get_url_content(self, content):

        """遍历所有的页面"""
        # myhtml = etree.HTML(content)
        parser = etree.HTMLParser()
        myhtml = etree.parse(StringIO(content), parser)
        div_list = myhtml.xpath("//div[@class='job-box']//ul/li")

        content_list = []

        for li in div_list[0:1]:
            item = {}
            # item["title"] = r.xpath("./a/text()")[0] if len(r.xpath("./a/text()"))>0 else None
            # item["href"] = r.xpath("./a/@href")[0] if len(r.xpath("./a/@href"))>0 else None
            # item["img_list"] = self.getimage_list(item["href"],[])
            # item["img_list"] = [requests.utils.unquote(i).split("&src=")[1] for i in item["img_list"]]

            href = self.baseurl + li.xpath("//div[@class='job-primary']//a/@href")
            title = li.xpath("//div[@class='job-primary']//a/div[@class='job-title']/text()")
            item = dict({"boss链接": href, "职位名称": title})
            item = self.get_details(item["boss链接"],item)
            time.sleep(random.random() * 5)

            content_list.append(item)


        next_url = content.xpath("//a[@ka='page-next']/@href")
        print("next_url:{}",next_url)
        return content_list,next_url

    def get_details(self,href,item):
        response = self.parse_url(href)

        item["城市"] = self.base_city
        item["薪资"] = response.xpath("//span[@class='salary']/text()").extract_first()
        item["学历要求"] = self.deal_em(response.xpath("//div[@class='job-banner']//p").extract())
        item["岗位福利"] = self.deal_with_dot(response.xpath("//div[@class='job-banner']//div[@class='job-tags']/span"))
        item["工作描述"] = self.deal_space_lst(response.xpath(
            "//div[@class='detail-content']//div[@class='job-sec'][1]/div[@class='text']/text()").extract())

        # item["团队介绍"] = self.deal_with_dot(response.xpath(
        #     "//div[@class='detail-content']//div[@class='job-sec'][2]/div[@class='job-tags']/span"))
        item["公司福利"] = self.deal_with_dot(
            response.xpath("//div[@class='detail-content']//div[@class='job-sec'][2]/div[@class='job-tags']/span"))
        item["公司名称"] = response.xpath(
            "//div[@class='sider-company']//a[@ka='job-detail-company_custompage']/text()").extract_first()
        item["融资情况"] = response.xpath(
            "//div[@class='sider-company']//i[@class='icon-stage']/../text()").extract_first()
        item["公司规模"] = response.xpath(
            "//div[@class='sider-company']//i[@class='icon-scale']/../text()").extract_first()
        item["公司行业"] = response.xpath(
            "//div[@class='sider-company']//a[@ka='job-detail-brandindustry']/text()").extract_first()
        item["公司地址"] = response.xpath("//div[@class='location-address']/text()").extract_first()
        # 抓取对应的图片的地址

        return item


    def save_content_list(self,content_list):
        # filePath = self.tiebaName+".txt"
        # with open(filePath,"a",encoding="utf-8") as f:
        #     for content in content_list:
        #         content = json.dumps(content,ensure_ascii=False,indent=2)
        #         f.write(content)
        #         f.write("\n")
        f = open(self.base_city + ".csv", mode="a", encoding="utf-8")
        writer = csv.writer(f)
        for item in content_list:
            keys = list(item.keys())
            # writer.writerow(keys)  # 将属性列表写入csv中
            # flag = False
            #  else:
            #     # 读取json数据的每一行，将values数据一次一行的写入csv中
            writer.writerow(list(item.values()))

        # spans 转成字逗号分隔字符串

    def deal_with_dot(self, spans):
        if spans:
            return ",".join([span.xpath("./text()").extract_first() for span in spans])
        else:
            return ""

    def deal_space_lst(self, elements):
        if isinstance(elements, list):
            return " ".join(elements)
        else:
            return ""

    def deal_em(self, element):
        elements = element[0].split('<em class="dolt"></em>')

        return elements


    def run(self):
        t1 = time.time()
        # 1 获取贴吧整个页面的标题以及对应标题的URL
        self.init_allUrl()
        next_url = self.start_url
        # while next_url:
            # 2 根据url去请求列表页面
        html = self.parse_url(next_url)
        # 2.1请求详情页面的地址
        content_list,next_url = self.get_url_content(html)
        # 3.做数据保存
        self.save_content_list(content_list)
        # 4.下一页数据的提取，重复上述循环


        print(time.time()-t1)


if __name__ == "__main__":
    teiba = baidu_tieba_jijian("成都2")
    teiba.run()
