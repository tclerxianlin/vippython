# 教育机构：马士兵教育
# 讲师：杨淑娟
# 开发时间：2022/4/25 10:05
#文件对象的常用方法：
'''
方法名：说明
read([size])从文件中读取size个字节或字符的内容返回，若省略[size]，则读取到文件末尾，即一次读取文件所有内容
readline():从文本文件中读取一行内容
readlines():把文本文件中每一行都作为独立的字符串对象，并将这些对象放入列表返回
write(str):将字符串str内容写入文件
writelines(s_list):把字符串列表s_list写入文本文件，不添加换行符
seek(offset[,whence]):
把文件指针移动到心得位置,offset表示相对于whence的位置
offset:为正往结束方向移动，为负往开始方向移动
whence不同的值代表不用的含义：
0：从文件头开始计算（默认值）
1：从当前位置开始计算
2：从文件尾开始计算
tell():返回文件指针的当前位置
flush():把缓冲区的内容写入文件，但不关闭文件
close():把缓冲区的内容写入文件，同时关闭文件，释放文件对象相关资源
'''
file=open('a.txt.txt','r')
#print(file.read(2))
#print(file.readline())
#print(file.readlines())
file.close()


