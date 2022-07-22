# 教育机构：马士兵教育
# 讲师：杨淑娟
# 开发时间：2022/4/13 0:00
#判断指定元素是否在列表中存在： 使用 in 与 not in
#格式：元素 in  列表名 ，元素 not in 列表名
#列表元素的遍历：
#格式： for 迭代变量 in 列表名：
print('P' in "Python")  #True
print("k" not in "Python") #True

lst = [10,20,'Python','hello']
print(10 in lst)    #True
print(100 in lst)    #False
print("P" in lst)    #False
print(10 not in lst) #False

print("----------------")
for item in lst:
    print(item)