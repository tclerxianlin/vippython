# 教育机构：马士兵教育
# 讲师：杨淑娟
# 开发时间：2022/4/19 10:50
#知识不熟练导致的错误
'''
1.索引越界问题IndexError
lst=[11,22,33,44]
print(lst[4])

2.append()方法的使用掌握不熟练
lst = []
lst =append('A','B','C')
print(lst)
'''

#知识点不熟悉导致错误的自查报点----->练练练

lst = [11,22,33,44]
print(lst[3])

lst=[]
tuple1=('A','B','C')
for i in tuple1:
    lst.append(i)
print(lst)