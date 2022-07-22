# 教育机构：马士兵教育
# 讲师：杨淑娟
# 开发时间：2022/4/19 20:14
#对象的创建又称为类的实例化   语法：实例名=类名（）
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


# 在类之外定义的称为函数，在之内定义的称为方法
def drink():
    print('喝水')

#创建Student类的对象
soul=Student('张三',20)
print(id(soul))
print(type(soul))
print(soul)
print('-------------------------------')
print(id(Student))
print(type(Student))
print(Student)
soul.eat()     #对象名.方法名（）
print(soul.name)
print(soul.age)

print('--------------')
Student.eat(soul)   #45行和40行的代码功能相同，都是调用Student中的eat方法
                     #类名.方法名（类的对象）----->实际上就是方法定义处的self