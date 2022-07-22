# 教育机构：马士兵教育
# 讲师：杨淑娟
# 开发时间：2022/4/17 18:34
#判断字符串操作的方法
'''
isidentifier():判断指定的字符串是不是合法的标识符
isspace():判断指定的字符串是否全部由空白字符组成（回车、换行，水平制表符）
isalpha():判断指定的字符串是否全部由字母组成
isdecimal():判断指定字符串是否全部由十进制的数字组成
isnumeric():判断指定的字符串是否全部由数字组成
isalnum():判断指定字符串是否全部由字母和数字组成
'''
s='hello,python'
print('1.',s.isidentifier())     #False
print('2',"hello".isidentifier())   #True
print('3.','张三_'.isidentifier())   #True
print('4',"123_张三".isidentifier())   #False

print('5',"\t".isspace())   #True

print('6','abc'.isalpha())   #True
print('7','张三四'.isalpha())   #True
print('8','张三1'.isalpha())    #False

print('9',"123".isdecimal())   #True
print('10','123四'.isdecimal()) #True
print('11','ⅡⅡⅡ'.isdecimal())   #False

print('12','123'.isnumeric())   #True
print('13','123四'.isnumeric())   #True
print('14','ⅢⅢⅢⅢ'.isnumeric())   #True

print('15','abc1'.isalnum())    #True
print('16','张三123'.isalnum())   #True
print('17','abc！'.isalnum())    #False