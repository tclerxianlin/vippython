# 教育机构：马士兵教育
# 讲师：杨淑娟
# 开发时间：2022/4/24 23:36
src_file=open('123.png','rb')
target_file=open('234.png','wb')
target_file.write(src_file.read())

src_file.close()
target_file.close()