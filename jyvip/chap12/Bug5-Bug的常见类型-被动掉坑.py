# 教育机构：马士兵教育
# 讲师：杨淑娟
# 开发时间：2022/4/19 11:09
#被动掉坑：程序代码逻辑没有错，只是因为用户错误操作或者一些'例外情况'而导致的程序崩溃
'''a = input('请输入第一个整数')
a = int(a)
b = input('请输入第二个整数')
b = int(b)
result=a/b
print('结果为',result)'''

#被动掉坑问题的解决方案：
'''Python提供了异常处理机制，可以再异常出现时即时捕获，然后内部'消化'，让程序继续运行
try:

    a = input('请输入第一个整数')
    a = int(a)
    b = input('请输入第二个整数')
    b = int(b)
    result=a/b
    print('结果为',result)
except ZeroDivisionError:
    print('对不起，除数不允许为0')
print('程序结束')

try:

    a = input('请输入第一个整数')
    a = int(a)
    b = input('请输入第二个整数')
    b = int(b)
    result=a/b
    print('结果为',result)
except ZeroDivisionError:
    print('对不起，除数不允许为0')
except ValueError:
    print('只能输入数字串')
print('程序结束')

'''
'''
多个except结构：
捕获异常的顺序按照先子类后父亲类的顺序，为了避免遗漏可能出现的异常，可以在最后增加BaseException

'''
try:
    n1=int(input('请输入一个整数：'))
    n2=int(input('请输入另一个整数:'))
    result=n1/n2
    print('结果为：',result)
except ZeroDivisionError:
    print('除数不能为0哦！')
except ValueError:
    print('不能将字符串转换为数字')
except BaseException as e:
    print(e)
