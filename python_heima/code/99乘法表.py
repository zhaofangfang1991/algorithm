# 打印99乘法表
i = 1
while i <=9:
    j = 1
    while j <= i:
        print("%d * %d = %d" %(j,i, i*j), end="\t")
        j = j+1
    print("")
    i = i+1


# 用嵌套打印小星星
row = 1
while row<=5:
    print("*" * row)
    row += 1
