# 教育机构：马士兵教育
# 讲师：杨淑娟
# 开发时间：2022/4/10 16:04
#转义字符
print("hello\nworld") # \ + 转移功能的首字母   n-->newline的首字符表示换行
print("hello\tworld")
print("helloooo\tworld")
print("hello\rworld")  #world将hello进行了覆盖
print("hello\bworld") #\b是退一个格，将o退没了

print("http:\\\\www.baidu.com")
print("老师说：“大家好”")

#原字符，不希望字符串中的转义字符起作用，就使用原字符，就是在字符串之前加上r或R
print(r"hello\nworld")
#注意事项，最后一个字符不能是反斜杠,2个可以
#print(r"hello\nworld\")
print(r"hello\nworld\\")

