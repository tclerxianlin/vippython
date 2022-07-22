# 教育机构：马士兵教育
# 讲师：杨淑娟
# 开发时间：2022/4/27 12:10
#金陵十二衩的前五位
'''
1变量的赋值
'''
name1='林黛玉'
name2='薛宝钗'
name3='贾迎春'
name4='贾探春'
name5='史湘云'
print('❶\t'+name1)
print('❷\t'+name2)
print('❸\t'+name3)
print('❹\t'+name4)
print('❺\t'+name5)

'''第二种方式'''
lst_name=['林黛玉','薛宝钗','贾元春','贾探春','史湘云']
lst_sig=['❶','❷','❸','❹','❺']
for i in range(5):
    print(lst_sig[i]+'\t'+lst_name[i])

'''第三种方式.字典'''
d={'❶':"林黛玉","❷":'薛宝钗','❸':'贾元春','❹':'贾探春','❺':'史湘云'}
print('---------------------------------------')
for key in d:
    print(key,d[key])
print('zip')
for s,name in zip(lst_sig,lst_name):    #打包成元组，在解包
    print(s,name)

