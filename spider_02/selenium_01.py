from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as expected
from selenium.webdriver.support.wait import WebDriverWait

def selenium_baidu():
    options = Options()
    options.add_argument('-headless')  # 无头参数
    driver = Firefox()  # 配了环境变量第一个参数就可以省了，不然传绝对路径
    wait = WebDriverWait(driver, timeout=10)
    driver.get('http://www.baidu.com')
    # wait.until(expected.visibility_of_element_located((By.ID, 'kw'))).send_keys(U"长城")
    # wait.until(expected.visibility_of_element_located((By.ID, 'su'))).click()
    driver.find_element_by_id("kw").send_keys(U"长城")
    driver.find_element_by_id("su").click()
    driver.implicitly_wait(10)
    # 获取新的页面快照
    driver.save_screenshot("长城.png")
    # print(driver.page_source)

    driver.find_element_by_id("kw").send_keys(Keys.CONTROL, "a")
    driver.find_element_by_id("kw").send_keys(Keys.CONTROL, "x")
    driver.find_element_by_id("kw").send_keys(u".netcore发展")
    driver.find_element_by_id("su").send_keys(Keys.RETURN)
    # 获取当前url

    print(driver.current_url)
    driver.save_screenshot("发展1.png")
    # driver.quit()

if __name__ == "__main__":
    pass



