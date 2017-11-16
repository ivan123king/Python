__author__ = 'lenovo'
#coding=utf-8

import pygal
from ch15.die import Die

#创建两个D6骰子
die_1 = Die()
die_2 = Die()

#掷骰子多次，并将结果存储到一个列表中
results = []
for roll_num in range(1000):
    result = die_1.roll()+die_2.roll()
    results.append(result)
#分析结果
frequencies = []
max_result = die_1 .num_sides+die_2.num_sides
for value in range(2,max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)
#分析结果可视化
hist = pygal.Bar()
hist.title = "Reuslts of Rolling two D6 dice 1000 times"
hist.x_labels = ['2','3','4','5','6','7','8','9','10','11','12']
hist.x_title = "Results"
hist.y_title = "Frequency of Result"
hist.add('D6+D6',frequencies)
hist.render_to_file('dice_visual.svg')
