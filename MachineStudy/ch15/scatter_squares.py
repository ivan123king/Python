__author__ = 'lenovo'
#coding=utf-8
import matplotlib.pyplot as plt

"""绘制散点图"""
x_values = [1,2,3,4,5]
y_values = [x**2 for x in x_values]
#绘制坐标分别是(1,1),(2,4),(3,9),(4,16),(5,25)
plt.scatter(x_values,y_values,edgecolors='none',s=50)#s是点的大小  edgecolors='none'删除数据点轮廓
#设置图表标题并给坐标轴加上标签
plt.title("Square Numbers",fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of Value",fontsize=14)

#设置刻度标记的大小
plt.tick_params(axis='both',which='major',labelsize=14)

#设置每个坐标轴的取值范围
plt.axis([0,100,0,100])

plt.show()