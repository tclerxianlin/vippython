# 教育机构：马士兵教育
# 讲师：杨淑娟
# 开发时间：2022/4/27 11:12
'''一.使用print方式进行输出（输出的目的地是文件）'''
fp=open('E:/vippython/chap19/test.txt','w')
print('奋斗成就更好的你',file=fp)
fp.close()

'''第二种方式，使用文件读写操作'''
with open('E:/vippython/chap19/test.txt','w') as file:
    file.write('奋斗成就更好地你')