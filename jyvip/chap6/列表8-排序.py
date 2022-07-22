# 教育机构：马士兵教育
# 讲师：杨淑娟
# 开发时间：2022/4/15 11:11
lst = [20,40,10,98,54]
print("排序前的列表",lst,id(lst))
#开始排序,调用列表对象的sort方法，默认是升序排序
lst.sort()
print("排序后的列表",lst,id(lst))

#通过指定关键字参数，将列表中的元素进行降序排序

lst.sort(reverse=True)  #reverse = True表示降序排序，reverse = False 就是升序排序
print(lst)
lst.sort(reverse = False)
print(lst)

print("-----------使用内置函数sorted()对列表进行排序，将产生一个新的列表对象-------------")
lst = [20,40,10,98,54]
print("原列表",lst)
#开始排序
new_list = sorted(lst)
print(lst)
print(new_list)
#指定关键字参数，实现列表元素的降序排序
desc_list = sorted(lst,reverse = True)
print(desc_list)


#两种方法的区别：sort()方法是对原列表进行一个排序操作，而内置函数sotred()是产生一个新的列表对象，而原列表对象不发生任何改变。

