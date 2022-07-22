# 教育机构：马士兵教育
# 讲师：杨淑娟
# 开发时间：2022/4/22 15:31
#Python中的包
'''
包是一个分层次的目录结构，它将一组功能相近的模块组织在一个目录下

作用：
代码规范和避免模块名称冲突

包与目录的区别：
包含__init__.py文件的目录称为包
目录里通常不包含__init__.py文件

包的导入：
import 包名.模块名
'''
'''在demo6的模块中导入package1 包'''
import package1.module_A  as ma      #ma是package1.module_A这个包中的模块的别名
#print(package1.module_A.a)
print(ma.a)