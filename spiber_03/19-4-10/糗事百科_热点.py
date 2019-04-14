# encoding:utf-8
import re,queue,json
from  urllib import request
from bs4 import BeautifulSoup

class GenSipder:

    items = list()
    def __init__(self,startUrl,domin):
        self.startUrl= startUrl
        self.baseUrl = domin
        self.data = self.parseUrl()


    '''解析链接'''
    def parseUrl(self):
        headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0"}
        next_page = self.startUrl

        while True:
            if next_page is None:
                break
            else:
                print(next_page)
                req = request.Request(next_page, headers=headers)
                content = self.openUrl(req)
                next_page = self.parseData(content)


    '''解析内容'''
    def parseData(self, content):
        # rule = re.compile(r'<div class="article block untagged mb15 .*?>(.*)</div>')
        # rule = re.compile(r'<div class="article block untagged mb15.*?></div>')
        # result = re.findall(rule,content)
        # print(result)
        if content:
            soup = BeautifulSoup(content)
            results = soup.find_all("div",attrs={'article' ,'block' ,'untagged','mb15'})
            GenSipder.items = list()
            for result in results:
                item = dict()
                item["author"] = result.find("div",attrs={'author'}).find('h2').text.replace("\n","")
                item["author-age"] = result.find("div", attrs={'author'}).find('div',attrs={'articleGender'}).text if  result.find("div", attrs={'author'}).find('div',attrs={'articleGender'}) else ""
                item["content"] = result.find("div",attrs='content').text.replace("\n","")
                item["content-img"] = result.find("div",attrs='thumb').find('img')["src"] if result.find("div",attrs='thumb') else ""
                item["vote"] = result.find("span", attrs='stats-vote').text.replace("\n","")
                item["comments"] = result.find("span", attrs='stats-comments').text.replace("\n","")
                GenSipder.items.append(item)
            self.saveContent()
            next = soup.find("span","next")
            if next.text.replace('\n','') == '下一页':
                next_page =self.baseUrl + soup.find("span","next").parent["href"]
            else:
                next_page = None
        return next_page

    '''存储到文档'''
    def saveContent(self):
        if len(GenSipder.items)>0:
            for item in GenSipder.items:
                jsonObj =json.dumps(item,ensure_ascii=False,indent=2)
                with open('糗事百科.txt','a',encoding="utf-8") as f:
                    f.write(jsonObj)

    def openUrl(self,url):
        response = request.urlopen(url)
        return response.read()

if __name__ == '__main__':
    genSipder = GenSipder("https://www.qiushibaike.com/hot/","https://www.qiushibaike.com")





