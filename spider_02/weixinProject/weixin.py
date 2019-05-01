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
            result.send_keys("test标题")
        else:
            print("未找到标题")
            return False

        # 找到正文
        result = findtag_tool.inter_time_find_tag_byFrame(self.webBrower,
                                                           "//body","ueditor_0", intertime=1, count=30)
        if result:
            print(result)
            result.send_keys("test正文")
            # result.send_keys("test正文")
        else:
            print("未找到正文")
            return False

        # 找到插入视频,首先从iframe中切换回来
        self.webBrower.switch_to.default_content()
        result = findtag_tool.inter_time_find_tag(self.webBrower, "//li[@id='js_editor_insertvideo']", intertime=1, count=30)
        if result:
            result.click()
        else:
            print("未找到插入视频")
            return False

        #找到上传视频的按钮
        result =findtag_tool.inter_time_find_tag(self.webBrower,
                                                 "//li[@class='weui-desktop-tab__nav']/a[contains(text(),'视频链接')]", intertime=1, count=30)

        if result:
            result.click()
        else:
            print("未找到插入")
            return False

        self.webBrower.find_element_by_name("videoLink").send_keys("https://v.qq.com/x/page/f0864buyf94.html")
        time.sleep(3)
        result = findtag_tool.inter_time_find_tag(self.webBrower,
                                                  "//div[@weui='true'][2]//button[contains(text(),'确定')]",
                                                  intertime=1, count=30)

        print(result.is_displayed())
        result.click()


if __name__ == '__main__':
    weixin = WeiXinUpload()
    weixin.login()
    # weixin.webBrower.close()