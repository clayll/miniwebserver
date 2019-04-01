from matplotlib import pyplot as plt, font_manager

myfont = font_manager.FontProperties(fname=r"c:\windows\fonts\msyhl.ttc")

y1 = [11,17,16,11,12,11,12,6,6,7,8,9,12,15,14,17,18,21,16,17,20,14,15,15,15,19,21,22,22,22,23]
y2 = [26,26,28,19,21,17,16,19,18,20,20,19,22,23,17,20,21,20,22,15,11,15,5,13,17,10,11,13,12,13,6]

x = range(31)
plt.figure(figsize = (20,8),dpi=100)
x_label = ["3月{}日".format(i+1) for i in x]
x1_label = ["" for i in range(10)]
x2_label = ["10月{}日".format(i+40) for i in x]
x_label.extend(x1_label)
x_label.extend(x2_label)
plt.xticks([i+1 for i in range(72)][::3],x_label[::3], fontproperties=myfont,rotation=45)

plt.scatter([i+1 for i in x][::3],y1[::3])
plt.scatter([i+40 for i in x][::3],y2[::3])
plt.show()

