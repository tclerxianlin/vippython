# 教育机构：马士兵教育
# 讲师：杨淑娟
# 开发时间：2022/4/12 23:29
#列表的查询操作
#1.获取列表中指定元素的索引，使用index()函数
'''如查列表中存在N个相同的源生，只返回相同元素中的第一个元素的索引
   如果查询的元素在列表中不存在，则会抛出ValueError
    还可以在指定的start和stop之间进行查找'''

lst = ["hello","world",98,'hello']
print(lst.index('hello'))  #如果列表中有相同元素只返回列表中相同元素的第一个元素的索引
#print(lst.index("Python"))      #valueError:"Python" is not in list
#print(lst.index('hello',1,3))   #valueError:"hello" is not in list     "world',98
print(lst.index('hello',1,4))    # 3

#获取列表中的单个元素：
'''正向索引从0到N-1,，逆向索引从-N到-1，指定索引不存在，抛出indexError
'''
lst = ['hello','world',98,'hello','world',234]

#获取索引为2的元素
print(lst[2])
#获取索引为-3的元素
print(lst[-3])

#获取索引为10的元素
#print(lst[10])  #IndexError: list index out of range

