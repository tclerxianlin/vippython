# 教育机构：马士兵教育
# 讲师：杨淑娟
# 开发时间：2022/4/22 15:50
'''
sys模块：与Python解释器及其环境操作相关的标准库
time模块：提供与时间相关的各种函数的标准库
os模块：提供了访问操作系统服务功能的标准库
calendar模块：提供与日期相关的各种函数的标准库
urllib模块------>实际上是一个包：用于读取来自晚上（服务器）的数据标准款------>爬虫的时候会用到
json模块：用于使用JSON序列化和反序列化对象
re模块：用于在字符串中执行正则表达式匹配和替换
math模块：提供标准算数运算函数的标准库
decimal模块：用于进行精确控制运算精度、有效数位和四舍五入操作的十进制运算
logging模块：提供了灵活的记录事件、错误、警告和调试信息等日志信息的功能
'''

import sys
#此方法获取对象所占的内存大小
print(sys.getsizeof(24))
print(sys.getsizeof(45))
print(sys.getsizeof(True))
print(sys.getsizeof(False))

import time
print(time.time())
print(time.localtime(time.time()))

import urllib.request
print(urllib.request.urlopen('http://www.baidu.com').read())

import math
print(math.pi)

