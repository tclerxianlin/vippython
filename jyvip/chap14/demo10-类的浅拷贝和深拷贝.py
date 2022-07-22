# 教育机构：马士兵教育
# 讲师：杨淑娟
# 开发时间：2022/4/22 11:25
#类的浅拷贝与深拷贝
'''
变量的赋值操作：只是形成两个变量，实际上还是指向同一个对象

浅拷贝：Python拷贝一般都是浅拷贝，拷贝时，对象包含的子对象的内容不拷贝。
       因此，源对象与拷贝对象会引用同一个子对象

深拷贝：使用copy模块的deepcopy函数，递归拷贝对象中包含的子对象，源对家和拷贝对象所有的子对象也不相同
'''

class CPU:
    pass
class Disk:
    pass
class Computer:
    def __init__(self,cpu,disk):
        self.cpu=cpu
        self.disk=disk
#(1)变量的赋值
cpu1=CPU()
cpu2=cpu1
print(cpu1,id(cpu1))
print(cpu2,id(cpu2))

#（2）类有浅拷贝
print('-----------------------')
disk=Disk() #创建一个硬盘类的对象
computer=Computer(cpu1,disk)  #创建一个计算机类的对象

#浅拷贝
import copy
print(disk)
computer2=copy.copy(computer)
print(computer,computer.cpu,computer.disk)
print(computer2,computer2.cpu,computer2.disk)

print('-------------------------------------------')
#深拷贝
computer3=copy.deepcopy(computer)
print(computer,computer.cpu,computer.disk)
print(computer3,computer3.cpu,computer3.disk)
