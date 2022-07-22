# 教育机构：马士兵教育
# 讲师：杨淑娟
# 开发时间：2022/4/11 19:35
#for-in循环：in 表达从（字符串、序列等）中一次取值，又称为遍历.遍历的对象必须是可迭代对象

for item in "Python": #第一次取出来的是P，将P赋值值item，将item的值输出
    print(item)

#range()产生一个整数序列---->也是一个可迭代对象
for i in range(10):
    print(i)

#如果在循环体中不需要使用到自定义变量，可将自定义变量为“_”
for _ in range(5):
    print("人生苦短，我用Python")

print("------------使用for循环，计算1到100之间的偶数和-------------------")
sum = 0 #用于存储偶数和
for item in range(1,101):
    if item % 2 == 0 :
        sum+=item
print("1到100之间的偶数和为",sum)

'''输出100到999之间的水仙花数
举例:
  153
   153 = 3*3*3+5*5*5+1*1*1
'''

for item in range(100,1000):
    x = item // 100
    y = item // 10 - x * 10
    z = item - x * 100 - y * 10
    a = x**3 + y**3 + z**3
    if a== item:
        print(item)

for z in range(100,1000):
    ge = z % 10 # 个位
    shi = z//10%10  #十位
    bai =z //100 # 百位
    a = ge**3 + shi**3 + bai**3
    if a== z:
        print(z)


