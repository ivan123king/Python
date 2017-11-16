__author__ = 'lenovo'
#coding=utf-8

import pygal
from ch15.die import Die

#创建一个D6和D10
die_1 = Die()
die_2 = Die(10)

results = [die_1.roll()+die_2.roll() for roll_num in range(1000)]
frequencies = [results.count(value) for value in range(2,die_1.num_sides+die_2.num_sides+1)]
print(results)
print(frequencies)

hist = pygal.Bar()
hist._title = "Results of D6 and D10 1000 times."
hist.x_labels = [str(value) for value in range(2,die_1.num_sides+die_2.num_sides+1)] #['2','3','4','5','6','7','8','9','10','11','12','13','14','15','16']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
# hist.add('D6+D10',frequencies)
# hist.render_to_file('different_dice3.svg')

def create_x_labels(min=1,max=6):
    print([str(value) for value in range(min,max+1)])

# create_x_labels()