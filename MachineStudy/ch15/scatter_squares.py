__author__ = 'lenovo'
#coding=utf-8
import matplotlib.pyplot as plt

"""绘制散点图"""
x_values = [1,2,3,4,5]
y_values = [x**2 for x in x_values]
#绘制坐标分别是(1,1),(2,4),(3,9),(4,16),(5,25)
#设置颜色 c=red c=(0,0,0.8)
# plt.scatter(x_values,y_values,c='red',edgecolor='none',s=50)#s是点的大小  edgecolors='none'删除数据点轮廓
#根据每个点的y值来设置颜色映射：就是渐变颜色  c指定根据什么值进行渐变
plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,edgecolor='none',s=50)
#设置图表标题并给坐标轴加上标签
plt.title("Square Numbers",fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of Value",fontsize=14)

#设置刻度标记的大小
plt.tick_params(axis='both',which='major',labelsize=14)

#设置每个坐标轴的取值范围
plt.axis([0,100,0,100])

plt.show()
#将图表保存到scatter_squares.py所在目录，保存为png图片，bbox_inches='tight'将周围多余空白区域裁剪掉
# plt.savefig('squares_plot.png',bbox_inches='tight');