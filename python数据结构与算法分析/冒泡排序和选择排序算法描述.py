# 冒泡排序
def bubbleSort(alist):
    for passnum in range(len(alist) - 1, 0, -1): # passnum就是趟数， range(start, stop, step)
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]

# 冒泡排序改进，某一趟没有做任何交换，说明序已经排好了。就结束排序。用exchanges做标记。
def shortBubbleSort(alist):
    exchanges = True
    passnum = len(alist) - 1
    while passnum > 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                exchanges = True
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
        passnum += 1

# 选择排序
def selectionSort(alist):
    for fillslot in range(len(alist) - 1, 0, -1):
        positionOfMax = 0
        for location in range(1, fillslot + 1):
            if alist[location] > alist[positionOfMax]:
                positionOfMax = location
        alist[fillslot], alist[positionOfMax] = alist[positionOfMax], alist[fillslot]


# 插入排序
def insertionSort(alist):
    for index in range(1, len(alist)):
        currentvalue = alist[index]
        position = index

        while position > 0 and alist[position - 1] > currentvalue:
            alist[position] = alist[position - 1]
            position = position - 1


        alist[position] = currentvalue


# 谢尔排序
def xierpaixu():
    pass


alist = [54,15,12,95,84,12,1,5,4,69]
bubbleSort(alist)
print(alist)

shortBubbleSort(alist)
print(alist)

selectionSort(alist)
print(alist)

insertionSort(alist)
print(alist)