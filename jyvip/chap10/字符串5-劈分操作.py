# 教育机构：马士兵教育
# 讲师：杨淑娟
# 开发时间：2022/4/17 18:21
#字符串劈分操作的方法：
'''
split(）方法：
从字符串的左边开始劈分，默认的劈分字符是空格字符串，返回的值都是一个列表
以通过参数sep指定劈分字符串是的劈分符
通过参数maxsplit指定劈分字符串时的最大劈分次数，在经过最大次劈分之后，剩余的子串会单独作为一部分

rsplit()方法：
从字符串的右边开始劈分，默认的劈分字符是空格字符串，返回的值都是一个列表
以通过参数sep指定劈分字符串是的劈分符
通过参数maxsplit指定劈分字符串时的最大劈分次数，在经过最大次劈分之后，剩余的子串会单独作为一部分
'''
s='hello world Python'
lst=s.split()
print(lst)
s1='hello,world,Python'
lst1=s1.split(",")
lst2=s1.split(sep=",")
print(lst1)
print(lst2)
print(s1.split(sep=",",maxsplit=1))

'''rsplit()从右侧开始劈分'''
print(s.split())
print(s1.rsplit(sep=","))
print(s1.rsplit(sep=",",maxsplit=1))
