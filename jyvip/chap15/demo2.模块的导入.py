# 教育机构：马士兵教育
# 讲师：杨淑娟
# 开发时间：2022/4/22 14:59
#自定义模块
'''
创建模块：新建一个.py文件，名称不要与Python自带的标准模块名称相同
导入模块

import 模块名称 [as 别名]
from 模块名称 import 函数/变量/类

'''

import math    #关于数学运算
print(id(math))
print(type(math))
print(math)
print(math.pi)
print('------------------------------------')
print(dir(math))
print(math.pow(2,3),type(math.pow(2,3)))
print(math.ceil(9.001))
print(math.floor(9.9999))


from math import pi
print(pi)
print(pow(2,3))
print(math.pow(2,3))
