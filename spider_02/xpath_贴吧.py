from lxml import etree
import requests,json,time
from pprint import pprint

class baidu_tieba_jijian():

    def __init__(self,kw):
        self.tiebaName = kw
        self.headers = {"User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"}
        self.url_list = []


    def init_allUrl(self):
        self.start_url = "m?kw={}&lp=5011&lm=&pn={}".format(self.tiebaName,0)
        self.baseurl ="https://tieba.baidu.com/mo/q---E43010237FA469B37C96EDE1EAD664A9%3AFG%3D1-sz%40320_240%2C-1-3-0--2--wapp_1551576146607_550/"
        # "https://tieba.baidu.com/mo/q---E43010237FA469B37C96EDE1EAD664A9%3AFG%3D1-sz%40320_240%2C-1-3-0--2--wapp_1551576146607_550/"

        self.url_list.append(self.start_url)

    def  parse_rul(self,url):

        url = self.baseurl + url

        response = requests.get(url, headers=self.headers)
        return response.content

    def get_url_content(self, html):

        """遍历所有的页面"""
        html = etree.HTML(html)
        div_list = html.xpath(r"//div/div[@class='i']")
        content_list = []

        for r in div_list:
            item = {}
            item["title"] = r.xpath("./a/text()")[0] if len(r.xpath("./a/text()"))>0 else None
            item["href"] = r.xpath("./a/@href")[0] if len(r.xpath("./a/@href"))>0 else None
            item["img_list"] = self.getimage_list(item["href"],[])
            item["img_list"] = [requests.utils.unquote(i).split("&src=")[1] for i in item["img_list"]]
            content_list.append(item)

        next_url = html.xpath("//div//a[@accesskey='6']/@href")[0] if len(html.xpath("//div//a[@accesskey='6']/@href"))>0 else None
        print("next_url:{}",next_url)
        return content_list,next_url

    def getimage_list(self,href,total_list:list):
        html = self.parse_rul(href)
        html = etree.HTML(html)
        # 抓取对应的图片的地址
        result = html.xpath("//img[@class='BDE_Image']/@src")
        for r in result:
            total_list.append(r)
        #抓取下一页的详情下一页的地址
        next_url = html.xpath("//div//a[@accesskey='6']/@href")[0] if len(html.xpath("//div//a[@accesskey='6']/@href"))>0 else None
        while next_url:
            return self.getimage_list(next_url,total_list)

        return total_list


    def save_content_list(self,content_list):
        filePath = self.tiebaName+".txt"
        with open(filePath,"a",encoding="utf-8") as f:
            for content in content_list:
                content = json.dumps(content,ensure_ascii=False,indent=2)
                f.write(content)
                f.write("\n")


    def run(self):
        t1 = time.time()
        # 1 获取贴吧整个页面的标题以及对应标题的URL
        self.init_allUrl()
        next_url = self.start_url
        while next_url:
            # 2 根据url去请求列表页面
            html = self.parse_rul(next_url)
            # 2.1请求详情页面的地址
            content_list,next_url = self.get_url_content(html)
            # 3.做数据保存
            self.save_content_list(content_list)
            # 4.下一页数据的提取，重复上述循环


        print(time.time()-t1)


if __name__ == "__main__":
    teiba = baidu_tieba_jijian("戳爷")
    teiba.run()
