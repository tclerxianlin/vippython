# 教育机构：马士兵教育
# 讲师：杨淑娟
# 开发时间：2022/4/26 23:47
with open('123.txt','w',encoding='utf-8') as file:
    file.write(str({'name':"张三",'成绩':20}))
with open('123.txt','r',encoding='utf-8') as rfile:
    wfile=rfile.readlines()
print(wfile)
for item in wfile:
    d = dict(eval(item))
    print(d)
print(type(d['成绩']))

