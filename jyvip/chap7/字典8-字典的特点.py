# 教育机构：马士兵教育
# 讲师：杨淑娟
# 开发时间：2022/4/17 11:07
#字典的特点：
#1.字典中的所有元素都是一个key-value对，key不允许重复，value可以重复
#2.字典中的元素是无序的，3.6后的版本就是有序的了
#3.字典中的key必须是不可变对象
#4字典也可以根据需要动态地伸缩
#5.字典会浪费较大的内存，是一种使用空间换时间的数据结构
d = {"name":"张三","name":"李四"}   #key不允许重复
print(d)

d ={"name":"张三","nikename":"张三"} #value可以重复的

lst = [10,20,30]
lst.insert(1,100)
print(lst)

d={lst:100}