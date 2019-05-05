#coding:utf-8
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import random

from selenium import webdriver
from bs4 import BeautifulSoup
from weixinProject.component_tools import scrollbar_tool
from weixinProject.wxtools.viewdao_tool import viewDao
# from component_tools.findtag_tool import inter_time_find_tag
from selenium.webdriver.chrome.options import Options
class TXView:
    def __init__(self):
        self.maxviewcount = 30
        self.flag = 'lrsp'
        #雷人视频最受好评
        self.url_leiren = "https://v.qq.com/x/list/fun?itype=8&icelebrity=-1&sort=5&iaspect=-1&icolumn=-1&offset=0"

        #self.url_zhenggu = "https://v.qq.com/x/list/fun?itype=3649&offset=0&icolumn=-1&sort=48&icelebrity=-1&iaspect=-1"
        #萌宝视频最新上架
        #self.url_mengbao = "https://v.qq.com/x/list/fun?itype=6&sort=5&offset=0&icelebrity=-1&icolumn=-1&iaspect=-1"   # #三个视频都要
        # self.url_lunxun = (self.url_leiren, self.url_zhenggu, self.url_mengbao)
        # self.url = {"lrsp":self.url_leiren , "zgsp":self.url_zhenggu, "mbsp":self.url_mengbao}
        self.viewmintime = u"00:00:30"
        self.viewmaxtime = u"00:02:00"
        self.viewcount = 0
        # chrome_options = Options()
        # chrome_options.add_argument('--headless')
        # self.viewdriver = webdriver.Chrome(chrome_options=chrome_options)
        self.viewdriver = webdriver.Firefox()
        #self.viewdriver = webdriver.Chrome()
        self.gxviewdb = viewDao()
        self.gxviewdbnames = self.gxviewdb.findviewname()
        # print(self.gxviewdbnames)

    def saveview(self, viewslist):
        for item in viewslist:
            self.gxviewdb.saveview(item)

    def judgeviewtime(self, viewitem):  # 筛选不符合时长的视频
        viewtime = viewitem.select(".figure_info_left")[0].get_text()
        return viewtime >= self.viewmintime and viewtime <= self.viewmaxtime

    def judgeviewrepeat(self, viewitem):  # 筛选重复的视频
        print(viewitem.select("img")[0].get("alt"))
        print(type(viewitem.select("img")[0].get("alt")))

        viewname = (viewitem.select("img")[0].get("alt").replace("\"", u"”").replace("\'", u"’").replace(":", u"：").replace("?", u"？"),)
        print(viewname[0])
        return viewname not in self.gxviewdbnames

    def nextpage(self):
        self.viewdriver.find_element_by_class_name("page_next").click()
        #inter_time_find_tag(self.viewdriver, "点击下一页", '//a[@class="page_next"]').click()

    def getview(self, viewslist):
        # 虽然是页面请求方式，但是新的页面展示的时候，有默认的图片，滚动条拉倒底端后才会有真正的图片
        self.viewdriver.maximize_window()#最大化浏览器
        scrollbar_tool.pullscrool(self.viewdriver, 0.03, 0.07)
        soup = BeautifulSoup(self.viewdriver.page_source, "lxml")#html.parser
        viewstag = soup.select(".list_item")  # 所有短视频

        for item in viewstag:
            if self.judgeviewtime(item) and self.judgeviewrepeat(item):  # 筛选视频时间和重复
                viewslist.append([
                    item.select("img")[0].get("alt").replace("\"", u"”").replace("\'", u"’").replace(":", u"：").replace("?", u"？"),  # 视频名字
                    item.select(".figure")[0].get("href"),#视频链接
                    "https:" + item.select("img")[0].get("src"), #视频图片链接
                    item.select(".figure_info_left")[0].get_text(),  # 视频时长
                    self.flag#视频类型
                ])
                self.viewcount += 1 #存到数据库的视频个数
                if self.viewcount >= self.maxviewcount:
                    break

        if self.viewcount < self.maxviewcount:#视频没抓够
            self.nextpage()
            print("下一页")
            self.getview(viewslist)

    def start(self):
        # 判断如果数据库中有8条数据，则不用再获取
        if self.gxviewdb.getUnPubulishCount()[0] > 8:
            self.viewdriver.close()
            return True


        self.viewdriver.get(self.url_leiren)
        viewslist = []
        print("开始")
        # self.viewdriver.get(self.url_leiren)
        # print("结束")

        # self.getview(viewslist)
        # self.saveview(viewslist)
        #self.flag = raw_input("雷人视频请输入1\n整蛊视频请输入2\n萌宝视频请输入3\n其它轮询抓取\n")
        # if self.flag != "1" or self.flag != "2" or self.flag != "3":
        #     pass
        #self.wxdriver.get(self.url.get(self.flag, self.url_lunxun))
        #self.flag = "lrsp"
        #self.viewdriver.get(self.url.get(self.flag, "error"))
        # self.gxviewdb.closegxviewdb()#关闭数据库
        self.getview(viewslist)
        for item in viewslist:
            self.gxviewdb.saveview(item)

        self.viewdriver.close()
        return True



if __name__ == '__main__':
    # txView = TXView()
    # list=[]
    # txView.getview(list)
    # print(list)
    # for item in list:
    #     txView.gxviewdb.saveview(item)
    #
    #
    # txView.viewdriver.close()
    pass