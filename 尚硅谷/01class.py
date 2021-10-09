'''
线性结构： 数组、队列、链表、栈
非线性结构：二维数组、多维数组、广义表、树、图

稀疏数组：
    五子棋的存盘操作，可缩小数组大小，只记录有效值，压缩了原数组；
    第一行记录 行 列 一共几个有效值
    后面的行   行 列  值


知识点：
1、python没有数组，可用列表
'''


def transfer1():
    '''
    1、定义一个二维数组，给二维数组，赋一些值作为初始值
    2、转稀疏数组
    :return:
    '''
    a = [ [0]*11 for i in range(11)]
    a[3][2] = 1
    a[2][4] = 2
    a[4][6] = 1

    # 创建一个满足条件的稀疏数组
    # 找到二维数组中一共有几个非零值
    sum = 0
    for j in range(11):
        for k in range(11):
            if a[j][k] != 0:
                sum += 1
    print('数组中一共有%d个有效值' %sum)

    # 开始创建稀疏数组 [sum+1][3]
    b = [ [0]*(3) for i in range(sum+1)]
    b[0][0] = sum+1
    b[0][1] = 3
    b[0][2] = sum
    count = 1
    for j in range(11):
        for k in range(11):
            if a[j][k] != 0:
                b[count][0] = j
                b[count][1] = k
                b[count][2] = a[j][k]
                count += 1


def transfer2():
    pass

def main():
    transfer1()  # 二维数据转稀疏数组

    transfer2()  # 稀疏数组转二维数组

if __name__ == '__main__':
    main()






