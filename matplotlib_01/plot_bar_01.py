from matplotlib import pyplot as plt, font_manager

myfont = font_manager.FontProperties(fname=r"c:\windows\fonts\msyhl.ttc")

plt.figure(figsize=(20,8),dpi=80)
# x = ["战狼2","速度与激情8","功夫瑜伽","西游伏妖篇","变形金刚5：最后的骑士","摔跤吧！爸爸","加勒比海盗5：死无对证","金刚：骷髅岛","极限特工：终极回归","生化危机6：终章","乘风破浪","神偷奶爸3","智取威虎山","大闹天竺","金刚狼3：殊死一战","蜘蛛侠：英雄归来","悟空传","银河护卫队2","情圣","新木乃伊",]
#
# y = [56.01,26.94,17.53,16.49,15.45,12.96,11.8,11.61,11.28,11.12,10.49,10.3,8.75,7.55,7.32,6.99,6.88,6.86,6.58,6.23]
#
# plt.xticks(list(range(20)),x,fontproperties = myfont)
# plt.bar(x,y,width=0.2,color='r')

a = ["猩球崛起3：终极之战","敦刻尔克","蜘蛛侠：英雄归来","战狼2"]
b_16 = [15746,312,4497,319]
b_15 = [12357,156,2045,168]
b_14 = [2358,399,2358,362]
_x = range(4)
_bar_width=0.2
plt.xticks([i+_bar_width for i in _x],a,fontproperties=myfont)

plt.bar(list(_x),b_14,width=_bar_width,color="c",label="9月14日")
plt.bar([i+_bar_width for i in _x],b_15,width=_bar_width,color="r",label="9月15日")
plt.bar([i+(_bar_width*2) for i in _x],b_16,width=_bar_width,label="9月16日")
plt.legend(prop=myfont)
plt.show()