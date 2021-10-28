# 队列：先进先出

class Queue(object):
    def __init__(self):
        self.items = []

    def enqueue(self, n):
        '''
        入队列
        入队尾
        :param n:
        :return:
        '''
        self.items.append(n)

    # 出队列
    def dequeue(self):
        return self.items.pop(0)

    # 判空
    def isEmpty(self):
        return self.items == []

    # 大小
    def size(self):
        return len(self.items)

q = Queue()

# print(q.isEmpty())
# q.enqueue(2)
# q.enqueue('hello')
# print(q.size())


