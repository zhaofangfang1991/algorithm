# 迭代累加
# 从1到N的累加，输出综合

def sum0Ton(n):
    sum = 0
    for i in range(1, n+1):
        sum += i

    return sum

sum = sum0Ton(100)
print(sum)

