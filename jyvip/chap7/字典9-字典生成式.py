# 教育机构：马士兵教育
# 讲师：杨淑娟
# 开发时间：2022/4/17 11:14
#字典生成式：items=['Fruit','Books','Others']  prices=[96,78,85]---->{"Fruit":96,"BOOKS":78,"OTHERS":85}
#内置函数zip()--->用于将可迭代对象作为参数，将对象中对应的元素打包成一个元组，然后返回这些元组组成的列表
items=["Fruits","Books","Others"]
prices=[96,78,85]
d = {item.upper() : price for item , price in zip(items,prices)}
print(d)


items=["Fruits","Books","Others"]
prices=[96,78,85,100,120]
d = {item.upper() : price for item , price in zip(items,prices)}
print(d)