

def solution1(a, b):
    c = a
    a = b
    b = c
    print("a = %d, b = %d" % (a, b))


def solution2(a, b):
    a = a + b
    b = a - b
    a = a - b
    print("a = %d, b = %d" % (a, b))


def solution3(a, b):
    a, b = b, a
    print("a = %d, b = %d" % (a, b))

solution1(10, 100)
solution2(10, 100)
solution3(10, 100)


