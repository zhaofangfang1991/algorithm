# python实现ADT 栈
# 也就是对栈的抽象实现
# 用列表来实现，假设栈顶在右侧

# 方式一：栈顶为尾端，遵循栈的先进后出原理，每次操作都是在尾端，时间复杂度O(1)
class Stack2(object):
    # 初始化
    def __init__(self):
        self.items = []

    # 判空
    def isEmpty(self):
        # if self.items == None:
        #     return True
        # return False

        return self.items == []

    # push
    def push(self, n):
        self.items.append(n)

    # pop
    def pop(self):
        return self.items.pop()

    # peek
    def peek(self):
        return self.items[-1]
        # return self.items[len(self.items) - 1]

    # size
    def size(self):
        return len(self.items)


# 方式二：栈顶在首端，为了遵循栈的先进后出的原理，每次操作push\pop时，需要移动整个栈，所以时间复杂度为O(n)
class Stack(object):
    # 初始化
    def __init__(self):
        self.items = []

    # 判空
    def isEmpty(self):
        return self.items == []

    # push
    def push(self, n):
        self.items.insert(0, n)

    # pop
    def pop(self):
        return self.items.pop(0)

    # peek
    def peek(self):
        return self.items[0]

    # size
    def size(self):
        return len(self.items)

# s = Stack2()
# print(s.isEmpty())
# s.push(4)
# s.push('dog')
# print(s.peek())
# s.push(True)
# print(s.size())
# print(s.isEmpty())
# s.push(8.4)
# print(s.pop())
# print(s.pop())
# print(s.size())
# print(s.peek())

