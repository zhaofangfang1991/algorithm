from 三python实现栈 import Stack2

# 方法1，只简单判断小括号
def parChecker(symbolString):
    s = Stack2()

    balanced = True
    index = 0

    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == '(':
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()
        index += 1


    if balanced and s.isEmpty():
        return True
    else:
        return False

# 方法2，判断所有种类的括号 ([{   }])
def parChecker2(symbolString):
    s = Stack2()

    balanced = True
    index = 0

    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in '([{':
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False
        index += 1


    if balanced and s.isEmpty():
        return True
    else:
        return False


def matches(open, close):
    opens = '([{'
    closes = ')]}'
    return opens.index(open) == closes.index(close)


print(parChecker('(((())))'))
print(parChecker('((())()'))

print(parChecker2('({([])})'))


