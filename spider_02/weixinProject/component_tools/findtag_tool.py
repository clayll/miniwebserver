#coding:utf-8
import time

def inter_time_find_tag(driver, tagname, strtag, intertime=1, count=30):
    nowcount = 0
    while nowcount < count:
        time.sleep(intertime)
        try:
            result = driver.find_element_by_xpath(strtag)
            print("规定时间内找到：" + tagname)
            return result  # 找到tag就返回
        except:
            nowcount += 1
            print( "没找到" + tagname + str(nowcount) + "次")

    print( "规定时间次数内没找到：" + tagname)