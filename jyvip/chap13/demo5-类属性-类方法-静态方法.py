# 教育机构：马士兵教育
# 讲师：杨淑娟
# 开发时间：2022/4/19 20:34
#类属性：类中方法外的变量称为类属性，被该类的所有对象所共享
#类方法：使用@classmethod修饰的方法，使用类名直接访问的方法
#静态方法：使用@stcticmethod修饰的方法，使用类名直接访问的方法
class Student:  # Student为类的名称（类名）由一个或多个单词组成，每个单词的首字母大写，其余小写
    native_pace = '吉林'  # 直接卸载类里的变量，称为类属性

    def __init__(self, name, age):  # 初始化方法
        self.name = name  # self.name称为实体属性，进行了一个赋值的操作，将局部变量的name的值赋给实体属性
        self.age = age


    # 实例方法
    def eat(self):
        print('学生在吃饭...')

    # 静态方法
    @staticmethod
    def method():
        print('我使用了statticmethod进行修饰，所以我是静态方法')

    # 类方法
    @classmethod
    def cm(cls):
        print('我是类方法，因为我使用了classmethod进行修饰')

#类属性的使用方式
print(Student.native_pace)
stu1=Student('张三',20)
stu2=Student('李四',30)
print(stu1.native_pace)
print(stu2.native_pace)
Student.native_pace='天津'
print(stu1.native_pace)
print(stu2.native_pace)

print('------------类方法的使用方式--------------')
Student.cm()
print('-----------静态的使用方式----------')
Student.method()