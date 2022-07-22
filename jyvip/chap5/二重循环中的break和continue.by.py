# 教育机构：马士兵教育
# 讲师：杨淑娟
# 开发时间：2022/4/12 10:26
#二重循环中的break和continue用于控制本层循环

'''流程控制语句break与continue在二重循环中的使用'''
for i in range(5):   #代表外层循环要执行5次
    for j in range(1,11):
        if j%2==0:
            break
        print(j)

for i in range(5):   #代表外层循环要执行5次
    for j in range(1,11):
        if j%2==0:
            continue
        print(j,end='\t')
    print()

