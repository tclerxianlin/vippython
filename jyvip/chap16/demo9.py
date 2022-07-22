# 教育机构：马士兵教育
# 讲师：杨淑娟
# 开发时间：2022/4/25 10:11
file=open('a.txt.txt','r')
#file.seek(1)     #汉字一个占两个字节,英文占一个字节，换行占两个字节
file.seek(2)
print(file.read())
print(file.tell())
file.close()