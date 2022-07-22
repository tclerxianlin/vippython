# 教育机构：马士兵教育
# 讲师：杨淑娟
# 开发时间：2022/4/20 19:57
#特殊属性：
'''名称：__dict__                  描述：获得类对象或实例对象所绑定的所有属性和方法的字典'''


print(dir(object))
class A:
    pass
class B:
    pass
class C(A,B):
    def __init__(self,name,age):
        self.name=name
        self.age=age
class D(A):
    pass
#创建C类的对象
x=C('Jack',20)   #x是C类型的一个实例对象
print(x.__dict__)     #实例对象的属性字典
print(C.__dict__)
print('---------------------')
print(x.__class__)    #<class '__main__.C'>输出了对象所属的类
print(C.__bases__)    #C类的父类类型的元素
print(C.__base__)      #C类的父类谁写在前面，就输出谁    类的基类
print(C.__mro__)     #类的层次结构
print(A.__subclasses__())    #子类的列表