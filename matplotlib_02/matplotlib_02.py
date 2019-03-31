from matplotlib import pyplot as plt,font_manager
import os



font = font_manager.FontProperties(fname=os.path.join("C:\Windows\Fonts\simfang.ttf"))
y =  [1,0,1,1,2,4,3,2,3,4,4,5,6,5,4,3,3,1,1,1]
y1 = [1,0,3,1,2,2,3,3,2,1 ,2,1,1,1,1,1,1,1,1,1]
x =  [i+11 for i in range(20)]
x_lable = ["{}岁".format(i+11) for i in range(20)]

plt.figure(figsize=(10,8))
plt.ylabel("朋友数量",fontproperties=font)
plt.xlabel("年纪",fontproperties=font)
plt.xticks(x,x_lable,fontproperties=font)
plt.plot(x,y,label="自己",color='c',linestyle='--')
plt.plot(x,y1,label ="同桌",color='r')
plt.grid(alpha=0.4)
plt.legend(prop=font,loc = "upper left")
plt.show()