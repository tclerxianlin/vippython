# 教育机构：马士兵教育
# 讲师：杨淑娟
# 开发时间：2022/4/17 11:22
#元组：Python内置的数据结构之一，是一个不可变序列
#不可变序列与可变序列
#不可变序列：字符串、元组，不可变序列没有增、删，改的操作
#可变序列：列表、字典，可变序列可以对序列执行增、删、改操作，对象地址不发生改变
'''不可变序列，可变序列'''
'''可变序列 列表，字典'''
lst=[10,20,45]
print(id(lst))
lst.append(300)
print(id(lst))

'''不可变序列，字符串，元组'''
s = 'hello'
print(id(s))
s = s+'worle'
print(id(s))