# 教育机构：马士兵教育
# 讲师：杨淑娟
# 开发时间：2022/4/24 23:02
#文件的读写原理：
'''
文件的读写俗称”IO操作“
文件读写操作流程：
Python操作文件---->打开或新建文件----->读、写文件------>关闭资源
操作原理：py文件----->解释器----->os(operation system)------>在硬盘上操作'''


'''
内置函数open()创建文件对象--------->程序（对象（映射磁盘上的真实文件））------->input 与 output---------->文件
通过IO流将磁盘文件中的内容与程序中的对象中的内容进行同步
语法规则：file=open(filename[,mode,encoding])
file---->被创建的文件对象
open------>创建文件对象的函数
filename--------->要创建或打开的文件的名称
mode------------->打开模式默认为只读
encoding---------->默认文本文件中字符的编码格式为gbk
'''
file = open('a.txt.txt','r')
print(file.readlines())            #readlines()读取文件中的鄋内容，输出的是一个类别
file.close()