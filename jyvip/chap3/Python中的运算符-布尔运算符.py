# 教育机构：马士兵教育
# 讲师：杨淑娟
# 开发时间：2022/4/11 15:07
#布尔运算符:对于布尔值之间的运算：and、or、not、in、not in
print('-------------and并且-----------')
a,b=1,2
print(a == 1 and b ==2) #True  True and True-->True
print(a==1 and b<2)#False True and False -->False
print(a!=1 and b==2)#False  False and True -->False
print(a!=1 and a!=2)#False  False and False -->False

print('--------or 或者---------')
print(a == 1 or b ==2) #True  True or True-->True
print(a==1 or b<2)#True True or False -->True
print(a!=1 or b==2)#True  False or True -->True
print(a!=1 or b!=2)#False  False or False -->False

print('-------not 对bool类型的操作数进行取反----------')
f = True
f2 =False
print(not f)
print(not f2)

print('-----------in 与 not in-------------- ')
s= 'helloworld'
print('w'in s)
print('k' in s)
print('w' not in s)
print('k' not in s)





