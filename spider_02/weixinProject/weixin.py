#coding:utf-8
from selenium import webdriver




class WeiXinUpload():
    def __init__(self):
        self.startUlr="https://mp.weixin.qq.com/"
        self.webBrower = webdriver.Firefox()

    def login(self):
        print("开始登录公众号")
        self.webBrower.get(self.startUlr)
        self.webBrower.find_element_by_name("account").send_keys("8238491@163.com")
        self.webBrower.find_element_by_name("password").send_keys("p9h4dumu")
        self.webBrower.find_element_by_class_name("btn_login").click()


if __name__ == '__main__':
    weixin = WeiXinUpload()
    weixin.login()