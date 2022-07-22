# 教育机构：马士兵教育
# 讲师：杨淑娟
# 开发时间：2022/4/17 16:21
#字符串中的大小写转换的方法

'''
upper()：把字符串中所有字符都转成大写字母
lower():把字符串中所有字符都转成小写字母
swapcase():把字符串所有大写字母转成小写字母，把所有小写字母转成大写字母
capitalize():把第一个字符转成大写，把其余字母转换成小写
title():吧每个单词的第一个字符串转换为大写，把每个单词的剩余字符转为小写
'''
s='hello,python'
a=s.upper()    #转成大写之后，会产生一个新的字符串对象
print(a,id(a))
print(s,id(s))

b=s.lower()   #转换之后，会产生一个新的字符串对象
print(b,id(b))
print(s,id(s))
print(b==s)
print(b is s)

s2='hello,Python'
print(s2.swapcase())

print(s2.title())

print(s2.capitalize())
