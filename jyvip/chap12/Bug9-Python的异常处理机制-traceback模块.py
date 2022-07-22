# 教育机构：马士兵教育
# 讲师：杨淑娟
# 开发时间：2022/4/19 11:43
#print(10/0)
import traceback
try:
    print("__________")
    print(1/0)
except:
    traceback.print_exc()