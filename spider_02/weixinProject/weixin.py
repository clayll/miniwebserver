#coding:utf-8
from selenium import webdriver
from component_tools import findtag_tool
import json
import time


class WeiXinUpload():
    def __init__(self):
        self.startUlr="https://mp.weixin.qq.com/"
        self.webBrower = webdriver.Firefox()

    def saveCookie(self):
        cookeis = self.webBrower.get_cookies()
        cookeisJson = json.dumps(cookeis,indent=2,ensure_ascii=False)
        with open("json.txt",mode='a+',encoding="utf-8") as f:
            f.write(cookeisJson)

    def setCookie(self,driver):
        try:
            with open("json.txt",mode="w") as f:
                cookeisJson = f.read()
            if cookeisJson:
                cookeisJson = json.loads(cookeisJson,encoding="utf-8")
                for cookiedct in cookeisJson:
                    driver.add_cookie(cookiedct)
        except Exception as ex:
            print("设置cooike异常:",ex)


    """
    微信登录功能
    """
    def login(self):
        print("开始登录公众号")
        self.webBrower.get(self.startUlr)
        self.setCookie(self.webBrower)
        self.webBrower.find_element_by_name("account").send_keys("8238491@163.com")
        self.webBrower.find_element_by_name("password").send_keys("p9h4dumu")
        self.webBrower.find_element_by_class_name("btn_login").click()
        self.saveCookie()

        # 跳转到新建群聊
        result = findtag_tool.inter_time_find_tag(self.webBrower,
            "//a[contains(text(),'新建群发')]", intertime=1, count=30)
        if result:
            # is_displayed()
            result.click()
            print("成功登录后跳转到新建群聊")
        else:
            print("登录跳转失败")
            return False

        # 再次跳转到自建图文
        result = findtag_tool.inter_time_find_tag_byNewUrl(self.webBrower,
            "//a/strong[contains(text(),'自建图文')]", intertime=1, count=30)
        if result:
            result.click()
            print("成功登录后跳转到自建图文")
        else:
            print("登录跳转自建图文失败")
            return False

        self.uploadVidoe()

    """上传视频"""
    def uploadVidoe(self):
        #找到标题
        result = findtag_tool.inter_time_find_tag_byNewUrl(self.webBrower,
                                            "//input[@id='title']", intertime=1, count=30)
        if result:
            result.sendkeys("test标题")
        else:
            print("未找到标题")
            return False

            # 找到标题
        result = findtag_tool.inter_time_find_tag_byFrame(self.webBrower,
                                                           "//div[contains(text(),'从这里开始写正文')]", intertime=1, count=30)
        if result:
            result.sendkeys("test正文")
        else:
            print("未找到标题")
            return False



if __name__ == '__main__':
    weixin = WeiXinUpload()
    weixin.login()
    # weixin.webBrower.close()