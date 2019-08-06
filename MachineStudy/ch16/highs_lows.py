__author__ = 'lenovo'
#coding=utf-8

import csv
filename = 'weather.csv'
with open(filename) as f:
    reader = csv.reader(f)
    # header_row = next(reader)#csv某块的方法，返回文件中下一行
    highs = []
    for row in reader:
        highs.append(int(row[1]))
    print(highs)
    # print(header_row)
    # for index,column_header in enumerate(header_row): #enumerate 返回此列表加了索引序列
    #     print(index,column_header)


