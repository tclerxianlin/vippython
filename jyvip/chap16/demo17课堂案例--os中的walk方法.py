# 教育机构：马士兵教育
# 讲师：杨淑娟
# 开发时间：2022/4/25 11:57
'''
walk文件会产生三元组  目录途径，目录名，文件名，每遍历一次，就往下走一级目录
'''
import os
path=os.getcwd()
lst_files=os.walk(path)
print(lst_files)
for dirpath,dirname,filename in lst_files:
    '''print(dirpath)
    print(dirname)
    print(filename)
    print('------------------------------')'''
    for dir in dirname:
        print(os.path.join(dirpath,dir))

    for file in filename:
        print(os.path.join(dirpath,file))
    print('-----------------------------------')