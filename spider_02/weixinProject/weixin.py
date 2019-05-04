#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common import keys
from wxtools import viewdao_tool,windows_tool
from component_tools import findtag_tool,scrollbar_tool
import json
import time
import txview

class WeiXinUpload():
    def __init__(self):
        self.startUlr="https://mp.weixin.qq.com/"
        self.webBrower = webdriver.Firefox()
        self.viewDao = viewdao_tool.viewDao()
        self.articles = list()
        # 发送信息的条数
        self.dataCount = 4

    def saveCookie(self):
        cookeis = self.webBrower.get_cookies()
        cookeisJson = json.dumps(cookeis,indent=2,ensure_ascii=False)
        with open("json.txt",mode='w',encoding="utf-8") as f:
            f.write(cookeisJson)

    def setCookie(self,driver):
        try:
            with open("json.txt",mode="r",encoding="utf-8") as f:
                cookeisJson = f.read()
            if cookeisJson:
                cookeisJson = json.loads(cookeisJson,encoding="utf-8")
                for cookiedct in cookeisJson:
                    driver.add_cookie({
                        'name': cookiedct["name"],
                        'value':cookiedct["value"],
                        'path':cookiedct["path"],
                        'domain':cookiedct["domain"],
                        'secure':cookiedct["secure"],
                        'httpOnly':cookiedct["httpOnly"],
                        'expiry':cookiedct["expiry"]

                    })
        except Exception as ex:
            print("设置cooike异常:",ex)


    """
    微信登录功能
    """
    def login(self):
        print("开始登录公众号")
        self.webBrower.get(self.startUlr)
        # 窗口最大化
        self.webBrower.maximize_window()
        self.setCookie(self.webBrower)
        self.webBrower.find_element_by_name("account").send_keys("8238491@163.com")
        self.webBrower.find_element_by_name("password").send_keys("p9h4dumu")
        self.webBrower.find_element_by_class_name("btn_login").click()
        self.saveCookie()

        # 查询要填充的数据
        self.articles = list(self.viewDao.findviewunused(self.dataCount))

        # 1跳转到新建群聊
        result = findtag_tool.inter_time_find_tag(self.webBrower,
            "/html/body/div[2]/div/div[2]/div/div/div[3]/div[2]/div[3]/div[1]/div[2]/a", intertime=1, count=30)
        if result:
            # is_displayed()
            result.click()
            print("成功登录后跳转到新建群聊")
        else:
            print("登录跳转失败")
            return False

        # 2再次跳转到自建图文
        result = findtag_tool.inter_time_find_tag_byNewUrl(self.webBrower,
            "//a/strong[contains(text(),'自建图文')]", intertime=1, count=30)
        if result:
            result.click()
            print("成功登录后跳转到自建图文")
        else:
            print("登录跳转自建图文失败")
            return False


    """上传视频"""
    def uploadVidoe(self, article):
        #1找到标题
        result = findtag_tool.inter_time_find_tag_byNewUrl(self.webBrower,"//input[@id='title']",
                                                  intertime=1, count=5)
        if result:
            result.send_keys(article[1])
        else:
            print("未找到标题")
            return False

        # 2找到正文
        result = findtag_tool.inter_time_find_tag_byFrame(self.webBrower,
                                                           "//body","ueditor_0", intertime=1, count=30)
        if result:

            result.send_keys(article[1])

        else:
            print("未找到正文")
            return False

        # 3找到插入视频,首先从iframe中切换回来
        self.webBrower.switch_to.default_content()
        result = findtag_tool.inter_time_find_tag(self.webBrower, "//li[@id='js_editor_insertvideo']", intertime=1, count=30)

        if result:
            result.click()
        else:
            print("未找到插入视频")
            return False

        #4 找到上传视频的tab页面
        # result =findtag_tool.inter_time_find_tag(self.webBrower,
        #                                          "//li[@class='weui-desktop-tab__nav']/a[contains(text(),'视频链接')]", intertime=1, count=30)
        result = self.webBrower.find_element_by_xpath("//div[@weui='true'][2]//ul[@class='weui-desktop-tab__navs']/li[2]/a")
        if result:
            result.click()
        else:
            print("未找到上传视频的tab页面")
            return False

        # 5插入视频链接
        result = self.webBrower.find_element_by_name("videoLink")
        result.send_keys(keys.Keys.CONTROL+"a")
        result.send_keys(article[2])

        # 6 插入视频后，点击确定
        result = findtag_tool.inter_time_find_tag(self.webBrower,
                                                  "//div[@weui='true'][2]//button[contains(text(),'确定')]",
                                                  intertime=1, count=30)

        result.click()
        print("素材插入成功！")

        #7开始选择封面
        action = ActionChains(self.webBrower)
        action.move_to_element(self.webBrower.find_element_by_id("js_cover_area")).perform()

        action.move_to_element(self.webBrower.find_element_by_id("js_imagedialog")).click().perform()


        self.webBrower.find_element_by_xpath("//div[@class='img_crop_panel']//div[@class='inner_main']/div[1]/div[1]/div[1]/span[1]/div[1]/label[1]").click()
        print("点击本地上传")

        # 8本地上传视频
        windows_tool.solvedexplore(article[3],dialogName=u'文件上传')

        #选择文件后点击下一步
        result = findtag_tool.inter_time_find_tag(self.webBrower,
                                         "//div[@class='dialog_ft']/span[1]/button",
                                         intertime=1, count=30)
        if result:
            result.click()
        else:
            print("未找到下一步")
            return False

        # 9选择文件后点击完成
        result = findtag_tool.inter_time_find_tag(self.webBrower,
                                                  "//div[@class='dialog_ft']/span[3]/button",
                                                  intertime=1, count=30)
        if result:
            result.click()
        else:
            print("未找到完成")
            return False

        # 10选择文件后点击保存
        self.webBrower.switch_to.default_content()
        result = findtag_tool.inter_time_find_tag(self.webBrower,"//div[@id='bottom_main']/div[4]/div[1]/span[@id='js_submit']",
                                                  intertime=1, count=30)
        if result:
            result.click()
            print("保存完成")
            time.sleep(3)
        else:
            print("未找到保存")
            return False

    """新建文章"""
    def addNewAticle(self):
        #1.找到添加文章按钮
        action = ActionChains(self.webBrower)
        action.move_to_element(self.webBrower.find_element_by_id("js_add_appmsg")).perform()
        action.move_to_element(self.webBrower.find_element_by_xpath("//div[@class='preview_media_add_panel']/ul/li[1]/a")).click().perform()

    """
    保存并群发 js_preview js_send
    """
    def sendAll(self):
        # 1 群发
        result = findtag_tool.inter_time_find_tag(self.webBrower,
                                                  "//div[@id='bottom_main']/div[4]/div[1]/span[@id='js_send']",
                                                  intertime=1, count=30)
        if result:
            result.click()
            print("保存到群发")
        else:
            print("未找到保存到群发")
            return False

        # 2 完成发送
        result = findtag_tool .inter_time_find_tag_byNewUrl(self.webBrower,
                                                  "//div[@id='send_btn_main']/div[1]/a",
                                                  intertime=1, count=5)
        if result:
            result.click()
            print("完成发送")

        else:
            print("未找到发送")
            return False

        # # 3 确认群发
        #
        # result = findtag_tool.inter_time_find_tag_byNewUrl(self.webBrower,
        #                                                    "//div[@id='wxDialog_1']/div[3]/a[1]",
        #                                                    intertime=1, count=5)
        # if result:
        #     result.click()
        #     print("完成继续群发")
        #     time.sleep(3)
        # else:
        #     print("未找到继续群发")
        #     return False

    @classmethod
    def sendMsgProcess(cls):
        if txview.TXView().start():
            weixin = WeiXinUpload()
            weixin.login()
            # 3 上传第一篇文章
            if weixin.uploadVidoe(weixin.articles[0]) == False:
                print("上传失败")
                return False

            for article in weixin.articles[1:]:
                weixin.addNewAticle()
                if weixin.uploadVidoe(article) == False:
                    print("上传失败")
                    return False

            if weixin.sendAll() == False:
                print("发送失败")
                return False

            # 发送成功后，更新状态

            weixin.viewDao.changeview(weixin.articles)

            print("此次操作完成！")
            # weixin.webBrower.close()


if __name__ == '__main__':
    WeiXinUpload.sendMsgProcess()




    # weixin.webBrower.close()
    # viewDao = viewdao_tool.viewDao()

    # datas = viewDao.findviewunused(8)
    # for data in datas[1:]:
    #     print(data[0])



