# 教育机构：马士兵教育
# 讲师：杨淑娟
# 开发时间：2022/4/18 17:01
def fun(a,b):
    c=a+b   #c，就称为局部变量，因为c是在函数体内定义的变量,a,b为函数的形参，作用范围也是函数内部，相当于局部变量

#print(c) ,因为a,c超出了起作用的范围
#print(a)

name='杨老师'     #name的作用范围为函数内部和外部都可以使用---->称为全局变量
print(name)
def fun2():
    print(name)
#调用函数
fun2()

def fun3():
    global age   #函数内部定义的变量，局部变量，局部变量使用global声明，这个变量实际上就变成了全局变量
    age=20
    print(age)
fun3()
print(age)
