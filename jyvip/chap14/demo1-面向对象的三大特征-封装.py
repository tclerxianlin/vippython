# 教育机构：马士兵教育
# 讲师：杨淑娟
# 开发时间：2022/4/20 11:04
#面向对象的三大特征：
'''
封装：提高程序的安全性
将数据（属性）和行为（方法）包装到类对象中。在方法内部对属性进行操作，在类对象的外部调用方法。
这样，无需关心方法内部的具体实现细节，从而隔离了复杂度。
在Python中没有专门的修饰符属于属性的私有，如果该属性不希望在类对象外部被访问，前面使用两个’__‘

继承：提高代码的复用性

多态：提高程序的可扩展性和可维护性
'''

class Car:
    def __init__(self,brand):
        self.brand=brand
    def start(self):
        print('汽车已启动')

car=Car('宝马X5')
car.start()
print(car.brand)

class Student:
    def __init__(self,name,age):
        self.name=name
        self.__age=age          #年龄不希望在类的外部被使用，所以加了两个

    def show(self):
        print(self.name,self.__age)

stu=Student('张三',20)
stu.show()
#在类的外部使用name与age
print(stu.name)
#print(stu.__age)     #果该属性不希望在类对象外部被访问，前面使用两个’__

#但也可以访问，纯靠程序员的自觉性
print(dir(stu))
print(stu._Student__age)     #在类的外部可以通过_Student__age进行访问




