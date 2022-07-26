# 教育机构：马士兵教育
# 讲师：杨淑娟
# 开发时间：2022/4/18 17:08
#什么是递归函数：如果在一个函数的函数体内调用了该函数本身，这个函数就称为递归函数
#递归的组成部分：递归调用与递归终止条件
#递归的调用过程：
'''每递归调用一次函数，都会在栈内存分配一个栈帧
每执行完一次函数，都会释放相应的空间'''
#递归的优缺点：
'''
缺点：占用内存多，效率低下
优点：思路和代码简单
'''
def fac(n):
    if n==1:
        return 1
    else:
        res = n*fac(n-1)
        return res
print(fac(6))
