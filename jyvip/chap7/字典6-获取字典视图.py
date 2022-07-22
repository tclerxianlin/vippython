# 教育机构：马士兵教育
# 讲师：杨淑娟
# 开发时间：2022/4/15 12:0
scores = {"张三":100,'李四':98,'王五':45}
#获取所有的key
keys=scores.keys()
print(keys)
print(type(keys))
print(list(keys))     #将所有的key组成的视图转成列表


#获取所有的value
values = scores.values()
print(values)
print(type(values))
print(list(values))

#获取所有的key-value对
items = scores.items()
print(items)
print(list(items))   #元组（）  #转换之后的列表元素是由元组组成的（元组将在下个章节讲解）


