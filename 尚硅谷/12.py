# 用数组模拟队列-向数组中添加数组

class Queue(object):

    def __init__(self, maxLength):
        self.maxLength = maxLength
        self.front = -1
        self.rear = -1
        self.list = list()


    # 创造队列
    def initQueue(self):
        self.list = list(self.maxLength)

    # 判断队列是否满
    def isFull(self):
        return self.rear == self.maxLength

    # 判断队列是否为空
    def isEmpty(self):
        return self.rear == self.front

    # 添加数据
    def addQueue(self, n):
        if self.isFull():
            return
        self.rear += 1
        print(len(self.list))
        print(self.list[0])
        # self.list[self.rear]  = n

    # 取数据，从头取一个数据
    def getData(self):
        if self.isEmpty():
            return
        self.front += 1
        print(self.front, type(self.front))
        print(self.list, type(self.list))

    # 显示队列所有数据
    def showQueue(self):
        if self.isEmpty():
            return
        for q in self.list:
            print("list(%d) = %d" % (q, list(q))) # 这里待修订

    # 显示队列的头数据,不是取数据
    def headQueue(self):
        if self.isEmpty():
            return
        print(self.list(self.front + 1))


# 验证
# q = Queue(5)
# print(q.isFull())
# print(q.isEmpty())
# q.addQueue(9)
# print(q.isEmpty())
# q.getData()



l = list()
l2 = list()

