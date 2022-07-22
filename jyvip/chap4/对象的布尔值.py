# 教育机构：马士兵教育
# 讲师：杨淑娟
# 开发时间：2022/4/11 16:22
#Python中的一切皆对象，所有对象都有一个布尔值
#获取对象的布尔值：使用内置函数bool()
#一下对象的布尔值为False
'''False、数值0、None、空字符串、空列表、空元组、空字典、空集合'''
print(bool(False))  #False
print(bool(0))     #False
print(bool(0.0))   #False
print(bool(None))  #False
print(bool(''))    #False
print(bool(""))    #False
print(bool([]))    #False空列表
print(bool(list()))  #False空列表
print(bool(()))   #False 空元组
print(bool(tuple()))  #False空元组
print(bool({}))    #空字典
print(bool(dict())) #空字典
print(bool(set()))  #空集合

print('----------其他对象的bool值均为True----------')
print(bool(18))
print(bool(True))
print(bool("helloworld"))





