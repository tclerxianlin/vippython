# 教育机构：马士兵教育
# 讲师：杨淑娟
# 开发时间：2022/4/11 17:13
'''从键盘录入两个整数，比较两个整数的大小'''
num_a = int(input("请输入第一个整数："))
num_b = int(input("请输入第二个整数："))
#比较大小
'''if num_a >= num_b:
    print(num_a,"大于等于",num_b)
else:
    print(num_a,'小于',num_b)'''


#条件表达式是if .....else的简写
#语法结构：
#x if 判断条件 else y
#运算规则：如果判断条件的布尔值为True，条件表达式的返回值为x，否则条件表达式的返回值为False

print("-----------使用条件表达式进入比较------")
print( (num_a,"大于等于",num_b) if num_a>=num_b else (num_a,"小于等于",numb))
print(num_a,"大于等于",num_b) if num_a>=num_b else print(num_a,"小于等于",numb)
print( (str(num_a)+"大于等于"+str(num_b)) if num_a>=num_b else (num_a,"小于等于",numb))
print( str(num_a)+"大于等于"+str(num_b) if num_a>=num_b else (num_a,"小于等于",numb))

