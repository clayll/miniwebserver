#coding:utf-8
import time

def inter_time_find_tag(driver, strtag, intertime=1, count=30):
    nowcount = 0
    while nowcount < count:
        time.sleep(intertime)
        try:
            result = driver.find_element_by_xpath(strtag)
            print("规定时间内找到：" + strtag)
            return result  # 找到tag就返回
        except:
            nowcount += 1
            print( "没找到" + strtag + str(nowcount) + "次")

    print( "规定时间次数内没找到：" + strtag)


"""
每找一次元素，都重新刷新一次url
"""
def inter_time_find_tag_byNewUrl(driver, strtag, intertime=1, count=30):
    nowcount = 0
    while nowcount < count:
        time.sleep(intertime)
        try:
            driver.switch_to.window(driver.window_handles[-1])

            result = driver.find_element_by_xpath(strtag)
            print("规定时间内找到：" + strtag)
            return result  # 找到tag就返回
        except:
            nowcount += 1
            print( "没找到" + strtag + str(nowcount) + "次")

    print( "规定时间次数内没找到：" + strtag)