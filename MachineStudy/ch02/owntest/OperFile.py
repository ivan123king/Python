__author__ = 'lenovo'
# -*- coding:utf-8 -*-
with open("d:\\ftp\\test.txt") as file_object:
    contents = file_object.readline()
    while contents:
        print(contents.rstrip())
        contents = file_object.readline()
