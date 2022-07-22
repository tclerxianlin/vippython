# 教育机构：马士兵教育
# 讲师：杨淑娟
# 开发时间：2022/4/25 10:35
#with语句（上下文管理器）
'''
with语句可以自动管理上下文资源，无论什么原因跳出with块，都能确保文件正确的关闭，以此来达到释放资源的目的
语法：with open('logo.png','rb') as src_file:
         src_file.read()
open('logo.png','rb')称为上下文表达式,结果为上下文管理器-------->同时创建一个运行时上下文
------->自动调用__enter__()方法，并将返回值赋值给src_file

实现了__enter()方法和__exit__（）方法-------->遵守了上下文管理协议

src_file.read():称为with语句体

离开运行时上下文，自动调用上下文管理器的特殊方法__exit__()

'''
print(type(open('a.txt.txt','r')))   #<class '_io.TextIOWrapper'>
with open('a.txt.txt','r') as file:
    print(file.read())