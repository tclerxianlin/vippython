# 教育机构：马士兵教育
# 讲师：杨淑娟
# 开发时间：2022/4/11 10:59
#浮点数整数部分和小数部分组成
a = 3.14159
print(a,type(a))
#浮点数存储不精确性：使用浮点数进行计算时，可能会出现小数位数不确定的情况
n1 = 1.1
n2 = 2.2
n3 = 2.1
print(n1+n2)
print(n3 + n1)

#解决方案：导入模块decimal
from decimal import Decimal
print(Decimal("1.1")+Decimal("2.2"))