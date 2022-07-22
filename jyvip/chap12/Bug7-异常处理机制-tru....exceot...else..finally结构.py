# 教育机构：马士兵教育
# 讲师：杨淑娟
# 开发时间：2022/4/19 11:33
#finally块无论是否发生异常都会被执行，能常用来释放try块中申请的资源
try:
    n1=int(input('请输入一个整数：'))
    n2=int(input('请输入另一个整数:'))
    result=n1/n2
except BaseException as e:
    print('出错了',e)
else:
    print('计算结果为',result)
finally:
    print('谢谢您的使用')