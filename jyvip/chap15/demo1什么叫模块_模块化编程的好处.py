# 教育机构：马士兵教育
# 讲师：杨淑娟
# 开发时间：2022/4/22 12:05
#模块：
'''
模块英文为Modules
函数与模块的关系---->一个模块中可以包含N多个函数
在Python中一个扩展名为.py的文件就是一个模块
使用模块的好处：
方便其他程序和脚本的导入并使用
避免函数名和变量名冲突
提高代码的可维护性
提高代码的可重用性
'''

'''Python程序有N多个包
   包中包含N多个模块A,模块B。。。。。。
   模块包括函数、类、语句.......
   类包括类属性、类方法、静态方法。。。。。。'''
print('今天也要加油呀！')
def fun():
    pass
def fun2():
    pass

class Student:
    native_place='吉林'#类属性
    def eat(self,name,age):
        self.name=name
        self.age=age
    @classmethod
    def cm(cls):
        pass

    @staticmethod
    def sm():
        pass

a=1
b=2
print(a+b)
