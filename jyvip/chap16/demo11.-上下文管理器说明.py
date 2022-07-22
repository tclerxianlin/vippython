# 教育机构：马士兵教育
# 讲师：杨淑娟
# 开发时间：2022/4/25 10:37
'''
MyContentMgr实现了特殊方法__enter__(),__exit__()称为该类对象遵守了上下文管理器协议
该类对象的实例对象，称为上下文管理器

MyContentMgr()
'''
class MyContentMgr(object):
    def __enter__(self):
        print('enter方法被调用执行了')
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit方法被调用执行了')

    def show(self):
        #print('show 方法被调用执行了',1/0)
        print('show,方法被调用执行了')

with MyContentMgr() as file: #相当于fileMyContentMgr()
    file.show()

#无论是否产生异常：都回去调用特殊方法，最后通过__exit__方法退出，这个退出我们就称作为自动的关闭了资源。