# 教育机构：马士兵教育
# 讲师：杨淑娟
# 开发时间：2022/4/19 11:28
'''
try...except..else结构：
如果try模块没有抛出异常，则执行else块，如果try中抛出异常，则执行except块
'''
try:
    n1=int(input('请输入一个整数：'))
    n2=int(input('请输入另一个整数:'))
    result=n1/n2
except BaseException as e:
    print('出错了',e)
else:
    print('计算结果为',result)

