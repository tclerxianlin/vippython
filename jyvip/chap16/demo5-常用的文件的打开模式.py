# 教育机构：马士兵教育
# 讲师：杨淑娟
# 开发时间：2022/4/24 23:20
#常用的文件打开模式
#文件的类型:
'''
按文件中数据的组织形式，文件分为以下两大类
文本文件：存储的是普通'字符'文本，默认为unicode字符集，可以使用记事本程序打开
二进制文件：把数据内容用'字节'进行存储，无法用记事本打开，必须使用专用的软件打开，举例：mp3音频文件，jpg图片，doc文档等
'''

#打开模式与描述：
'''
r:以只读模式打开文件，文件的指针将会放在文件的开头
w：以只写模式打开文件，如果文件不存在则创建，如果文件存在，则覆盖原有内容，文件指针在文件的开头
a:以追加模式打开文件，如果文件不存在则创建，文件指针在文件开头。如果文件存在， 则在文件末尾追加内容，文件指针在原文件末尾
b:以二进制方式打开文件，不能单独使用，需要与其他模式一起使用,rb,或者wb
+:以读写方式打开文件，不能单独使用，需要与其他模式一起使用,a+
'''
file = open('b.txt','w')
file.write('python')         #readlines()读取文件中的鄋内容，输出的是一个类别
file.close()