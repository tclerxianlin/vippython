# 教育机构：马士兵教育
# 讲师：杨淑娟
# 开发时间：2022/4/25 11:38
#os.path模块操作目录相关函数
'''
函数：说明
abspath(path):用于获取文件或目录的绝对路径
exists(path):用于判断文件或目录是否存在，如果存在返回True,否则返回False
join(path,name)：将目录与目录或者文件名拼接起来
splitext():分离文件名和扩展名
basename(path):从一个目录中提取文件名
dirname(path):从一个路径中提取文件路径,不包括文件名
isdir(path):用于判断是否为路径
'''
import os.path
print(os.path.abspath('demo13.py'))
print(os.path.abspath('break语句.py'))
print(os.path.exists('demo14.py'),os.path.exists('demo18.py'),os.path.exists('calc.py'))
print(os.path.join('E://Python','demo13.py'))
print(os.path.split('demo13.py'))
print(os.path.split('E:\\vippython\\chap15\\demo13.py'))
print(os.path.splitext('demo13.py'))
print(os.path.basename('E:\\vippython\\chap15\\demo13.py'))
print(os.path.dirname('E:\\vippython\\chap15\\demo13.py'))
print(os.path.isdir('E:\\vippython\\chap15\\demo13.py'))