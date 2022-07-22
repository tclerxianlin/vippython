# 教育机构：马士兵教育
# 讲师：杨淑娟
# 开发时间：2022/4/20 11:55
#object类
'''
object类是所有类的父类，因此所有类都有object类的属性和方法。
内置函数dir()可以查看指定对象所有属性
Object有一个__str__()方法，用于返回一个对于"对象的描述",对应于内置函数str()经常用于print()方法，帮我们查看对象的信息，
所以我们经常会对__str__()进行重写
'''
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return  '我的名字是{0}，今年{1}岁'.format(self.name,self.age)
stu=Student('张三',20)
print(dir(stu))
print(stu)     #默认会调用__str__()这样的方法，__str__（）方法被重写了
print(type(stu))