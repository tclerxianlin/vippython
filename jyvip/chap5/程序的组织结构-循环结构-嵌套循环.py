# 教育机构：马士兵教育
# 讲师：杨淑娟
# 开发时间：2022/4/12 10:15
#嵌套循环：循环结构中又嵌套了另外的完整的循环结构，其中内层循环作为外层循环的循环体执行
'''输出一个三行四列的矩形'''
for i in range(1,4):   #行表，执行三次，一次是一行
    for j in range(1,5):
        print("*",end="\t") #不换行输出
    print() #换行


