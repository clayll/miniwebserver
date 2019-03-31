from matplotlib import pyplot as plt
import random,os
import matplotlib


font = matplotlib.font_manager.FontProperties(fname=os.path.join("C:\Windows\Fonts\simfang.ttf"))

x = range(2,26,2)
y = [15,13,14.5,17,20,25,26,26,27,22,18,15]

fig = plt.figure(figsize=(20,8),dpi=80)

# plt.xticks([i/2 for i in range(4,49)][::3])
print(matplotlib.matplotlib_fname() )#将会获得matplotlib包所在文件夹

a = [random.randint(20,35) for i in range(120)]
b = [i for i in range(120)]
b_label = [ '10点{}分钟'.format(i) for i in range(60)][::3]
b_label += [ '11点{}分钟'.format(i) for i in range(60)][::3]
plt.xticks(b[::3],b_label,rotation=40,fontproperties=font)
plt.plot(b[::3],a[::3])
plt.xlabel("时间",fontproperties=font)
plt.ylabel("温度",fontproperties=font)
# plt.savefig("s1_size.png")
plt.show()