__author__ = 'lenovo'
#coding=utf-8

import matplotlib.pyplot as plt
from ch15.random_walk import RandomWalk

#创建RandomWalk实例，并将包含的点都绘制出来
while True:
    rw = RandomWalk()
    rw.fill_walk()
    #设置绘图窗口的尺寸  figure需要放在scatter方法前，否则绘制两个图表，一个为空白
    #figure(dpi=128,figsize=(10,6)) 使用dpi设置分辨率
    plt.figure(figsize=(10,6))
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values,rw.y_values,c=point_numbers,cmap=plt.cm.Blues,edgecolor='none',s=15)
    #突出起点和终点
    plt.scatter(0,0,c='green',edgecolors='none',s=100)
    plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolors='none',s=100)
    #隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk?(y/n)")
    if keep_running.lower() == 'n':
        break