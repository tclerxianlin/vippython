# 教育机构：马士兵教育
# 讲师：杨淑娟
# 开发时间：2022/4/17 15:17
#两个集合是否相等：可以用运算符==或！=进行判断
#一个集合是否是另一个集合的子集L可以调用方法issubset进行判断
#一个集合是否是另一个集合的超集，可以调用方法issuperset进行判断
#两个集合是否没有交集：可以调用方法isdisjoint进行判断

'''两个集合是否相等（元素相同，就相等，因为集合无序）'''
s={10,20,30,40}
s2={30,40,20,10}
print(s==s2)      #True
print(s!=s2)      #False

'''一个集合是否是另一个集合的子集'''
s1={10,20,30,40,50,60}
s2 ={10,20,30,40}
s3={10,20,90}
print(s2.issubset(s1))#True
print(s3.issubset(s1)) #False

'''一个集合是否是另一个集合的超集'''
print(s1.issuperset(s2))       #True
print(s1.issuperset(s3))    #False

'''两个集合是否毫无相关'''
print(s2.isdisjoint(s3))  #False,说明有交集
s4={100,200,300}
print(s2.isdisjoint(s4))#True