# 教育机构：马士兵教育
# 讲师：杨淑娟
# 开发时间：2022/4/22 16:25
#第三方模块的安装及使用
'''
第三方模块的安装：
pip install 模块名

第三方模块的使用：
import 模块名
'''
import schedule
import time

def job():
    print('哈哈——————————————')

schedule.every(3).seconds.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)

