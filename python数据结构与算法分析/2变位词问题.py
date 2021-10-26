# 变位词问题
# 解题思路: 写一个bool函数，以两个词作为参数，返回两个词是否为变位词

def isB(a, b):
    if len(a) != len(b):
        return False

    for aa in a:
        if aa not in b:
            return False
    return True


result = isB('heart4', '4earth')
print(result)