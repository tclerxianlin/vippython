# 教育机构：马士兵教育
# 讲师：杨淑娟
# 开发时间：2022/4/10 15:44
# 可以输出数字
print(520)
print(98.5)

# 可以输出字符串
print("helloworld")

# 含有运算符的表达式
print(3 + 1)  # 3和1叫做操作数，+叫做运算符

# 将数据输出文件中  注意点，1.所指定的盘符得存在2.使用file = fp（变量名），否则写不进去
fp = open('E:/text.txt','a+') #"a+"的意思，如果文件不存在就创建，存在就在文件内容的后面继续追加，看运行了几次
print("helloworld",file=fp)
fp.close()

#不进行换行输出（输出内容在一行当中）
print("hello","world","Python")

