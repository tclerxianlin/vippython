# 教育机构：马士兵教育
# 讲师：杨淑娟
# 开发时间：2022/4/17 18:51
#字符串替换
'''
replace()方法：第1个参数指定被替换的子字符串，第2个参数指定替换子字符串的字符串，该方法返回替换后得到的字符串，
替换前的字符串不发生变化，调用该方法时可以通过第三个参数指定最大替换次数
'''
#字符串的合并
'''
join()方法：将列表或元组中的字符串合并成一个字符串
'''
s='hello,Python'
print(s.replace('Python','Java'))
print(s)

s1='hello,Python,Python,Python'
print(s1.replace('Python','Java',2))

s2='hello,Python'
print(s2.replace('Python','JavaC+++++++'))


lst=['hello','java','Python']
print('|'.join(lst))
print(''.join(lst))

t=('hello','java','Python')
print(''.join(t))

print("*".join('Python'))


