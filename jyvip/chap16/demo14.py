# 教育机构：马士兵教育
# 讲师：杨淑娟
# 开发时间：2022/4/25 11:04
#os模块操作目录相关函数
'''
getcwd():返回当前的工作目录
listdir(path):返回指定路径下的文件和目录信息
mkdir(path[,mode])  创建目录
makedirs(path1/path2...[,mode])    创建多级目录
rmdir(path)           删除目录
removedirs(path1/path2.....)删除多级目录
chdir(path)    将path设置为当前工作目录
'''
import os
print(os.getcwd())

#lst = os.listdir('../chap16')
#print(lst)

#os.mkdir('newdir2')

#os.makedirs('A/B/C')
#os.rmdir('newdir2')
#os.removedirs('A/B/C')

os.chdir('E:\\vippython\\chap16')
print(os.getcwd())
