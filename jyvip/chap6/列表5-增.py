# 教育机构：马士兵教育
# 讲师：杨淑娟
# 开发时间：2022/4/13 0:08
#列表元素的增加操作：

#向列表的末尾添加一个元素
lst = [10,20,30]
print("添加元素之前",lst,id(lst))
lst.append(100)
print("添加元素之后",lst,id(lst))

#在列表的末尾至少添加一个元素
lst2 = ["hello","world"]
#lst.append(lst2)   #将lst2作为一个元素添加到列表的末尾
#向列表的末尾一次性添加多个元素
lst.extend(lst2)
print(lst)

#在列表的任意位置添加一个元素
lst.insert(1,90)
print(lst)


#在列表的任意位置添加至少一个元素
#使用切片，把切掉的地方用新的列表代替
lst3 = [True,False,"hello"]
lst[1:]=lst3
print(lst)
