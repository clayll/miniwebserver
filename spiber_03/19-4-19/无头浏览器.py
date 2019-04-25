from bs4 import BeautifulSoup
import pprint
from selenium import webdriver

browser = webdriver.Firefox()
pprint.pprint(browser.__dict__.items(),width=5)
browser.get("http://www.baidu.com")

browser.close()



a = 6082
b = 6110
s = b -a

print(s*5*4)