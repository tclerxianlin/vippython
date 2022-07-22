# 教育机构：马士兵教育
# 讲师：杨淑娟
# 开发时间：2022/4/11 16:32
#选择结构：程序根据判断条件的布尔值选择性地执行部分代码，明确的让计算机知道在什么条件下，该去做什么

#单分支结构，缩进代表层次结构
money = 1000 #余额
s = int(input("请输入取款金额：")) #取款金额
#判断余额是否充足
if money >= s:
    money = money - s
    print("取款成功，余额为：",money)

#双分支结构：if...else,二选一执行
'''从键盘录入一个整数，编写程序让计算机判断是奇数还是偶数'''
num = int(input("请输入一个整数"))

#条件判断
if num % 2 == 0:
    print(num,"是偶数")
else:
    print(num,"是奇数")

#多分支结构：处理连续区间段问题，多选一执行
'''
从键盘录入一个整数  成绩
90- 100  A
80 - 89 B
70 - 79 C
60 - 69 D
0 - 59 E
小于0或大于100为非法数据(不是成绩的有限范围)
'''
score = int(input("请输入一个成绩："))
#判断
if score >= 90 and score <= 100:
    print("A级")
elif score >= 80 and score <= 89:
    print('B级')
elif score >=70 and score <=79:
    print('C级')
elif score >= 60 and score <= 69:
    print('D级')
elif 0 <= score <= 59:
    print('E级')
else:
    print("对不起，成绩有误，不在成绩的有效范围")






