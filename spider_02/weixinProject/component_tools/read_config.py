import configparser
import os
import time

# 获取config.ini的路径
config_path =os.path.join(os.path.abspath(""),'app.cfg')
conf = configparser.ConfigParser()
conf.read(config_path)
# print(config_path)
# print(conf.sections())
def getAppSection(key,model='loginApp'):
    return conf.get(model, key)

def setAppSection(key,value,model='loginApp'):
    conf.set(model, key, value)
    conf.write(open(config_path, 'w'))

"""设置第一次登录的时间"""
def setAppFirstLogin(url):
    setAppSection("logindate",time.strftime('%Y-%m-%d'))
    setAppSection("cookiewithurl",url)



