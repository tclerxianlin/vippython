# 教育机构：马士兵教育
# 讲师：杨淑娟
# 开发时间：2022/4/17 20:22
#字符串的比较操作：
'''
运算符：>,>=,<,<=,==,!=
比较规则：首先比较两个字符串中的第一个字符，如果相等则继续比较下一个字符，依次比较下去，直到两个字符串中的
字符不相等时，其比较结果就是两个字符串的比较结果，两个字符串中的所有后续字符将不再被比较

比较原理：两上字符进行比较时，比较的是其ordinal value（原始值），调用内置函数ord可以得到指定字符的
ordinal value。与内置函数ord对应的是内置函数chr，调用内置函数chr时指定ordinal value可以得到其对应的字符
'''

print('apple'>'app')    #True
print('apple'>'banana')   #False,相当于97>98 ------>False
print(ord('a'),ord('b'))

print(chr(97),chr(98))

'''==与is的区别
==比较的是value
is 比较的是id是否相等
'''

a=b='Python'
c='Python'
print(a==b)    #True
print(b==c)    #True

print(a is b)  #True
print(a is c)  #True

