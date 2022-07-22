# 教育机构：马士兵教育
# 讲师：杨淑娟
# 开发时间：2022/4/25 10:56
#os模块与操作系统相关的一个模块

'''
os模块是Python内置的与操作系统功能和文件系统相关的模块，该模块中的语句
的执行结果通常与操作系统有关，在不同的操作系统上运行，得到的结果可能不一样

os模块与os.path模块用于对目录或文件进行操作
'''
import os
#os.system('notepad.exe')     打开记事本
#os.system('calc.exe')           打开计算器

#直接调用可执行文件
os.startfile('C:\\Program Files (x86)\\Tencent\\QQ\\Bin\\qq.exe')   #打开qq运行界面