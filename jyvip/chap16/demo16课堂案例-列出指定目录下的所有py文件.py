# 教育机构：马士兵教育
# 讲师：杨淑娟
# 开发时间：2022/4/25 11:52
#列出指定目录下的所有py文件
import os
path=os.getcwd()
lst=os.listdir(path)
for filename in lst:
    if filename.endswith('.py'):
        print(filename)