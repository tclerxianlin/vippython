# 教育机构：马士兵教育
# 讲师：杨淑娟
# 开发时间：2022/4/25 10:09
file=open('a.txt.txt','a')
#file.write('hello')
lst = ['java','python','go']
file.writelines(lst)
file.close()