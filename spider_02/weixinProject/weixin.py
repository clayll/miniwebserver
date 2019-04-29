#coding:utf-8
from selenium import webdriver
from component_tools import findtag_tool
import time
import json





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
            with open("json.txt",mode="r") as f:
                cookeisJson = f.read()
            if cookeisJson:
                cookeisJson = json.loads(cookeisJson,encoding="utf-8")
                for cookiedct in cookeisJson:
                    driver.add_cookie(cookiedct)
        except Exception as ex:
            print("设置cooike异常:",ex)



    def login(self):
        print("开始登录公众号")
        self.webBrower.get(self.startUlr)
        self.setCookie(self.webBrower)
        self.webBrower.find_element_by_name("account").send_keys("8238491@163.com")
        self.webBrower.find_element_by_name("password").send_keys("p9h4dumu")

        print(type(self.webBrower.find_element_by_class_name("btn_login")))
        self.webBrower.find_element_by_class_name("btn_login").click()

        print("成功登录后跳转到新建群聊")
        self.saveCookie()
        reuslt = findtag_tool.inter_time_find_tag_byNewUrl(self.webBrower,
            "//a[contains(text(),'新建群发')]", intertime=1, count=30)
        if reuslt:

            reuslt.click()
        else:
            print("登录跳转失败")



if __name__ == '__main__':
    weixin = WeiXinUpload()
    weixin.login()
    # weixin.webBrower.close()