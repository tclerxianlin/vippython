# 教育机构：马士兵教育
# 讲师：杨淑娟
# 开发时间：2022/4/20 11:41
#方法重写
'''
如果子类对继承自父类的某个属性或方法不满意，可以再子类中对其（方法体）进行重新编写
子类重写后的方法中可以通过super().xxx()调用父类中被重写的方法
'''
class Person(object):  #Person继承object类
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(self.name,self.age)

class Student(Person):
    def __init__(self,name,age,stu_no):
        super().__init__(name,age)
        self.stu_no=stu_no
    def info(self):

        super().info()
        print(self.stu_no)


class Teacher(Person):
    def __init__(self,name,age,teachofyear):
        super().__init__(name,age)
        self.teachofyear=teachofyear
    def info(self):
        super().info()
        print(self.teachofyear)


stu=Student('张三',20,'1001')
teacher=Teacher('李四',34,10)

stu.info()
teacher.info()