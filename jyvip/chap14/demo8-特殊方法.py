# 教育机构：马士兵教育
# 讲师：杨淑娟
# 开发时间：2022/4/20 20:17
#特殊方法：
'''
__len__()             通过重写__len__（）方法，让内置函数len()的参数可以是自定义类型
__add__()              通过重写__add__（）方法，可使用自定义对象具有"+"功能
__new__()              用于创建对象
__init__()            对创建的对象进行初始化'''

a=20
b=100
c=a+b    #两个整数类型
d=a.__add__(b)
print(c)
print(d)

class Student:
    def __init__(self,name):
        self.name=name
    def __add__(self, other):
        return self.name+other.name
    def __len__(self):
        return len(self.name)
stu1=Student('张三')
stu2=Student('李四')

s=stu1+stu2     #实现了两个对象的加法运算（因为在Student类中  编写__add__()特殊的方法）
print(s)

s=stu1.__add__(stu2)
print(s)

print('—————————————————————————')
lst=[11,22,33,44]
print(len(lst))   #len是内置函数len
print(lst.__len__())
print(len(stu1))

