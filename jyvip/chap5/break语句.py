# 教育机构：马士兵教育
# 讲师：杨淑娟
# 开发时间：2022/4/11 19:57
#break 语句：用于结束循环结构，通常与分支结构if一起使用
"""从键盘录入密码，最多录入3次，如果正确就结束循环"""
for item in range(3):
    pwd =input("请输入密码")
    if pwd =="8888":
        print("密码正确")
        break
    else:
        print("密码不正确")

a = 0
while a<3:
    """条件执行体（循环体）"""
    pwd=input("请输入密码：")
    if pwd == '8888':
        print("密码正确")
        break
    else:
        print("密码不正确")

