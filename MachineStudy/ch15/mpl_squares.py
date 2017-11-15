__author__ = 'lenovo'
#coding=utf-8

import matplotlib.pyplot as plt
"""绘制折线图"""
input_values = [1,2,3,4,5]#输入值
squares = [1,4,9,16,25]#输出值
plt.plot(input_values,squares,lineWidth=5)  #根据列表中数字绘制图形
#设置图表标题，并给坐标轴加上标签
plt.title("Square Numbers",fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of Value",fontsize=14)

#设置刻度标记大小
plt.tick_params(axis='both',labelsize=14)

plt.show() # 打开matplotlib查看器


