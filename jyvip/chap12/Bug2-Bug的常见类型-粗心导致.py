# 教育机构：马士兵教育
# 讲师：杨淑娟
# 开发时间：2022/4/19 10:38
#Bug常见类型：1.粗心导致错误   （SyntaxError）
#粗心导致错误的自查宝典：
'''
1.漏了末尾的冒号，如if语句，循环语句，else子句等
2.缩进错误，该缩进的没缩进，不该缩进的瞎缩进
3.把英文符号写成中文符号，比如说：引号，冒号，括号
4.字符串拼接的时候，把字符串和数字拼在一起
5.没有定义变量，比如说while的循环条件的变量
6.“==”比较运算符和'='赋值运算符的混用
'''
age=input('请输入你的年龄')
print(type(age))
if int(age)>=18:
    print('成年人......')

i = 0
while i <10:
    print(i)
    i+=1

for i in range(3):
    unmae=input('请输入用户名')
    pwd=input("请输入密码：")
    if unmae=="admin" and pwd =='admin':
        print('登入成功！')
        break
    else:
        print("输入有误")
else:
    print('对不起，三次均输入错误')

