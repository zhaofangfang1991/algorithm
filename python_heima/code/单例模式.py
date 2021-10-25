# 重写__new__方法
class Single(object):
    def __new__(cls, *args, **kwargs): # __new__作用：1、给对象分配内存空间  2、返回对象的引用
        print('我在__new__内部重写函数')
        return super().__new__(cls)

    def __init__(self):
        print('这里是初始化方法')


s1 = Single()
print(s1)