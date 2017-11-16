__author__ = 'lenovo'
#coding=utf-8
import pygal
from ch15.die import Die

#创建一个D6,表示6面的骰子
die = Die()
#掷几次骰子，并将结果存储在一个列表中
results = []
for roll_num in range(10000):
    result = die.roll()
    results.append(result)
# print(results)
#结果分析
frequencies = []
for value in range(1,die.num_sides+1):
    frequency = results.count(value)#count() 方法用于统计字符串里某个字符（value）出现的次数。可选参数为在字符串搜索的开始与结束位置。
                                    #  此处用来统计1至6数字出现次数
    frequencies.append(frequency)
print(frequencies)
#对结果进行可视化
hist = pygal.Bar()#创建柱状图
hist.title = "Results of rolling one D6 1000 times:"
hist.x_labels = ['1','2','3','4','5','6']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add('D6',frequencies)#将值添加到图表中
hist.render_to_file('die_visual.svg')#将图表渲染为SVG文件
