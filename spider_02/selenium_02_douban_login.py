import time,os
from selenium.webdriver import Firefox
from selenium.webdriver.support import expected_conditions as expected
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

class douban_login():

    def __init__(self):
        self.driver = Firefox()

    def __del__(self):
        pass
        # self.driver.quit()

    def login(self):

        wait = WebDriverWait( self.driver, timeout=10)
        self.driver.get('https://accounts.douban.com/passport/login_popup?login_source=anony')

        self.saveCookie(self.driver.get_cookies())
        try:

            # wait.until(expected.visibility_of_element_located((By.ID, 'kw'))).send_keys(U"长城")
            # wait.until(expected.visibility_of_element_located((By.ID, 'su'))).click()
            # self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/ul[1]/li[2]").click()
            # wait.until(expected.visibility_of_element_located((By.XPATH, "//li[start-with(@class,'account-tab-account')]")))
            self.driver.find_element_by_xpath("//ul/li[2]").click()

            self.driver.implicitly_wait(100)
            self.driver.find_element_by_id("username").send_keys(u"20960180@qq.com")
            self.driver.find_element_by_id("password").send_keys(u"p9h4dumu")
            self.driver.find_element_by_link_text("登录豆瓣").click()

            self.saveCookie(self.driver.get_cookies())

        except Exception as ex:
            print(ex)

    def saveCookie(self,cookies):

        path = os.path.join(os.path.abspath(""),"file","cookie","douban.txt")
        print(path)
        with open(path,"a") as f:
            f.write(time.strftime("%Y-%m-%d %X", time.localtime()))
            f.write('\n')
            f.write(r"*"*80)
            for c in cookies:
                f.write('\n')
                f.write(str(c))



if __name__ == "__main__":
    d = douban_login()
    d.login()
