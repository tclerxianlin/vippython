# 教育机构：马士兵教育
# 讲师：杨淑娟
# 开发时间：2022/4/11 11:54
#输入函数input
present = input('大圣想要什么礼物呢？')
print(present,type(present))


#从键盘录入两个整数，计算两个整数的和
a = input('请输入一个加数:')
b = input('请输入另一个加数：')
print(type(a),type(b))
print(a+b)  #因为input输入的类型是str，此时加号起的是连接作用

c = input("请输入一个加数：")
d = input("请输入另一个加数：")
e = int(input("输入最后一个加数："))
c = int(c)
d = int(d)
print(type(c),type(d))
print(c+d)
print(c+e)

