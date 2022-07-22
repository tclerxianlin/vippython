# 教育机构：马士兵教育
# 讲师：杨淑娟
# 开发时间：2022/4/15 11:51
'''获取字典的元素'''
scores = {"张三":100,'李四':98,'王五':45}
'''第一种方式，使用[]'''
print(scores['张三'])
#print(scores['陈六'])  #KeyError: '陈六'

'''第二种方式，使用get()方法'''
print(scores.get('张三'))
print(scores.get('陈六'))   #None
print(scores.get('马',99))   #99是在查找'马'所对应的value值不存在时，提供的一个默认值

#[]取值与使用get()取值的区别
#1.[]如果字典中不存在指定的key，抛出keyError异常
#2.get（）方法取值，如果字典中不存在指定的key，并不会抛出KeyError而是返回None,可以通过参数设置默认的value，以便指定的Key不存在时返回。
