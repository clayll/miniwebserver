#coding:utf-8
import random
import time

def pullscrool(driver, mintime, maxtime):
    js = '''
   function RandomNumBoth(Min, Max){
   var Range = Max - Min;
   var Rand = Math.random();
   var num = Min + Math.round(Rand * Range);
   return num;}

   oldscrollpos = window.scrollY;
   step = RandomNumBoth(80, 100);
   window.scrollBy(0, step);
   newscrolpos = window.scrollY;
   if(oldscrollpos == newscrolpos)
       return false;
   else
       return true;
   '''
    while driver.execute_script(js):
        time.sleep(random.uniform(mintime, maxtime))# 取随机值更人性化