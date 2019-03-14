from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.firefox.options import Options
# from selenium.webdriver.support import expected_conditions as expected
# from selenium.webdriver.support.wait import WebDriverWait
#
# if __name__ == "__main__":
#     options = Options()
#     options.add_argument('-headless')  # 无头参数
#     driver = Firefox(executable_path=r'C:\Program Files\Mozilla Firefox\\firefox.exe', firefox_options=options)  # 配了环境变量第一个参数就可以省了，不然传绝对路径
#     wait = WebDriverWait(driver, timeout=10)
#     driver.get('http://www.baidu.com')
#     wait.until(expected.visibility_of_element_located((By.NAME, 'q'))).send_keys('headless firefox' + Keys.ENTER)
#     wait.until(expected.visibility_of_element_located((By.CSS_SELECTOR, '#ires a'))).click()
#     print(driver.page_source)
#     driver.quit()

options = Options()
options.add_argument('-headless')  # 无头参数
driver = Chrome(chrome_options=options)

driver.get('http://www.baidu.com')