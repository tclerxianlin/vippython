# 教育机构：马士兵教育
# 讲师：杨淑娟
# 开发时间：2022/4/11 10:43
#变量可以多次赋值，多次赋值之后，变量名会指向新的空间。原来的则变为内存垃圾
name="马里亚"
print(id(name))
name ="楚溜冰"
name="马里亚"
print(id(name))

