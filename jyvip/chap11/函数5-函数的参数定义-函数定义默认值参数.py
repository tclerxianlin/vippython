# 教育机构：马士兵教育
# 讲师：杨淑娟
# 开发时间：2022/4/18 16:11
#函数定义默认值参数：函数定义时，给形参设置默认值，只有与默认值不符的时候才需要传递实参
def fun(a,b=10):    #b称为默认值参数
    print(a,b)

#函数的调用
fun(100)
fun(20,30)

print()
print('hello',end='\t')
print('world')


