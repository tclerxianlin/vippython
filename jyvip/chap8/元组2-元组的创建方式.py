# 教育机构：马士兵教育
# 讲师：杨淑娟
# 开发时间：2022/4/17 11:29
'''元组的创建方式'''
'''第一种，使用()'''
t = ('Python','world',98)
print(t)
print(type(t))

t2 = 'Python','world',98   #省略了小括号
print(t2)
print(type(t2))

t3=('Python',)#如果元组中只有一个元素，逗号不能省
print(t3)
print(type(t3))

'''第二种创建方式，使用内置函数tuple（）'''
t1=tuple(('Python','world',98))
print(t1)
print(type(t1))

'''空列表的创建方式
   空字典的创建方式
   空元组的创建方式'''
lst=[]
lst1=list()

d={}
d2=dict()

t4 =()
t5 =tuple()
print("空列表",lst,lst1)
print("空字典",d,d2)
print("空元组",t4,t5)
