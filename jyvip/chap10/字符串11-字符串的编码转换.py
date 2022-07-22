# 教育机构：马士兵教育
# 讲师：杨淑娟
# 开发时间：2022/4/18 11:39
#字符串的编码转：
#变法与解码的方式：
#编码：将字符串转换为二进制数据（Bites)
#解码：将bites类型的数据转换成字符串类型
s = '天涯共此时'
#编码
print(s.encode(encoding='GBK'))    #在GBK这种编码格中，一个中文占两个字节
print(s.encode(encoding='UTF-8'))  #在UTF-8这种编辑格式中，一个中文占三个字节

#解码
#byte达标的就是一个二进制数据（字节类型数据）
byte=s.encode(encoding='GBK')
print(byte.decode(encoding='GBK'))

byte=s.encode(encoding='UTF-8')
print(byte.decode(encoding='UTF-8'))



