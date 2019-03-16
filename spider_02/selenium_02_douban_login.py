import time,os,json,threading
from selenium.webdriver import Firefox
from selenium.webdriver.support import expected_conditions as expected
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from queue import Queue

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

class douyu_01():
    def __init__(self,url,fileName):
        self.driver = Firefox()
        self.url = url
        self.filePath = os.path.join(os.path.abspath("file"),fileName)
        self.q = Queue()

    def __del__(self):
        self.driver.quit()

    def getDouyuRoomInfo(self):
        self.driver.get(self.url)
        for x in range(5):
            self.driver.implicitly_wait(300)
            try:
                items = self.driver.find_elements_by_xpath("//a[@class='DyListCover-wrap']")

                item = {}
                for i in items:
                    item["intro"] = i.find_element_by_xpath(".//h3[@class='DyListCover-intro']").text
                    item["img"]=i.find_element_by_xpath(".//img").get_attribute("src")
                    item["zone"]=i.find_element_by_xpath(".//span[@class='DyListCover-zone']").text
                    item["user"] = i.find_element_by_xpath(".//h2[@class='DyListCover-user']").text
                    item["hot"] = i.find_element_by_xpath(".//span[@class='DyListCover-hot']").text
                    self.q.put(item)
            except Exception as ex:
                print(ex)

            self.driver.find_elements_by_xpath("//span[@class='dy-Pagination-item-custom']")[1].click()

    def saveDouYuContentThread(self):

        while True:
            try:
                item = self.q.get()

                with open(self.filePath,"a",encoding="utf-8") as f:
                    f.write(json.dumps(item,indent=2,ensure_ascii=False))
                    f.write("\n")
                self.q.task_done()
            except Exception as ex:
                print(ex)

    def saveDouYuContent(self,item):
        with open(self.filePath, "a") as f:
            f.write(json.dumps(item,indent=2))


if __name__ == "__main__":
    # d = douban_login()
    # d.login()
    d = douyu_01("https://www.douyu.com/directory/all","直播.txt")
    # threading.Thread(target=d.getDouyuRoomInfo).start()
    for x in range(3):
        t = threading.Thread(target=d.saveDouYuContentThread)
        t.setDaemon(True)
        t.start()

    d.getDouyuRoomInfo()



    d.q.join()
    print("--end--")
