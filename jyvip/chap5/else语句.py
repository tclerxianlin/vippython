# 教育机构：马士兵教育
# 讲师：杨淑娟
# 开发时间：2022/4/12 10:07
#else语句：与else语句配合使用的三种情况
'''1，if条件表达式不成立时执行else        if......else......
 2.没有碰到break时跳出循环体时候执行else      while ......else         for ...... else.....
 '''

for item in range(3):
    pwd = input("请输入密码：")
    if pwd =="8888":
        print("密码正确")
        break
    else:
        print("密码不正确")
else:
    print("对不起，三次密码均输入错误")

a = 0
while a<3:
    pwd = input("请输入密码：")
    if pwd == "8888":
        print("密码正确")
        break
    else:
        print("密码不正确")
    a +=1
else:
    print("对不起，三次密码均输入错误")
