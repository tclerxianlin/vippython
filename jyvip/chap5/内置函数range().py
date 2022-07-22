# 教育机构：马士兵教育
# 讲师：杨淑娟
# 开发时间：2022/4/11 17:38
#内置函数：不需要前面加任何前缀，直接可以使用的函数
#range()函数，用于生成一个整数序列
#返回值为一个迭代器的对象
"""range类型的优点：不管range对象表示的整数序列有多长，所有range对象占用的内存空间都是相通的，因为仅仅需要存储start,stop和step
，只有当用到range对象时，才会去计算序列中的相关元素

"""
#in 与 not in 判断整数序列中是否存在（不存在）指定的整数
#range()的三种创建方式

'''第一种创建方式，只有一个参数(小括号中只给一个数)'''
r = range(10)  #[0,1,2,3,4,5,6,7,8,9],默认从0开始，默认相差1称为步长
print(r)
print(list(r)) #用于查看range对象中的整数序列---->list是列表的意思

'''第二种创建方式，给了两个参数(小括号中给了两个数)'''
r = range(1,10)  #给定了起始值，从1开始，到10结束（不包括10）,默认步长为1
print(list(r))   #[1,2,3,4,5,6,7,8,9]
'''第三种创建方式，给了三个参数（小括号中给了三个数）'''
r = range(1,10,2)
print(list(r)) #[1,3,5,7,9]



'''判断指定的整数，在序列中是否存在  in, not in'''
print(10 in r)   #False,10不在当前的r这个整数序列中
print(9 in r)    #True,9在当前的r这个序列中

print(10 not in r)  #True
print(9 not in r)  #False




