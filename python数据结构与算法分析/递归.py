# 递归-把问题转换成规模更小的相同问题
# 给定一个列表，返回所有数的和
'''
列表中数的个数不定，需要一个循环和一个累加变量来迭代求和
'''

def sum(n):
    # 解法1，利用循环
    # sum = 0
    # for i in range(n+1):
    #     sum += i
    # return sum

    # 解法2 利用递归
    sum = 0
    num = n - 1
    if num == 1:
        return 1
    else:
        sum = sum(num)
    return

# print(sum(100))



# 列表求和解法1：for循环
def listSum(list):
    sum = 0
    for i in list:
        sum += i
    return sum

# 列表求和解法2：递归解法
def listSum2(list):
    if len(list) == 1:
        return list[0]
    else:
        return list[0] + listSum2(list[1:])



print(listSum([1,2,3,4,5,6,7,8,6,5,5,3,5]))
print(listSum2([1,2,3,4,5,6,7,8,6,5,5,3,5]))
