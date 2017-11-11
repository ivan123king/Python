__author__ = 'lenovo'
# -*- coding: utf-8 -*-
'''
from ch02.owntest import Dog
这里Dog引入的是模块不是类
调用类Dog.Dog
如果要引入类需要：from ch02.owntest.Dog import Dog

'''
# from ch02.owntest import Dog
from ch02.owntest.Dog import Dog

class NorthDog(Dog):
    def __init__(self,name,age):
        # super(NorthDog, self).__init__(name,age);
        super().__init__(name,age);
    def increment_age(self,incre_age=0):
        self.age += incre_age;
        print(self.age)

north_dog = NorthDog('north',7);
north_dog.increment_age(22)