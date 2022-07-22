# 教育机构：马士兵教育
# 讲师：杨淑娟
# 开发时间：2022/4/25 10:48
with open('123.png','rb') as src_file:
    with open('456.png','wb') as target_file:
        target_file.write(src_file.read())