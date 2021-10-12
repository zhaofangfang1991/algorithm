# 石头剪刀布
# 1 > 2    2>3  3>1
dict = {
    1: '石头',
    2: '剪刀',
    3: '布'
}
while True:
    # 玩家
    num = int(input("石头1 剪刀2 布3"))
    print("玩家选择的拳头是： %s" % dict[num])

    # 电脑
    import random
    computer = random.randint(1,3)
    print("电脑出的是： %s" %dict[computer])

    if num == computer:
        print("本局平局")
    elif ((num == 1 and computer == 2)
          or (num == 2 and computer == 3)
          or (num == 3 and computer == 1)):
        print("本局胜利的是 玩家")
    else:
        print("本局胜利的是 电脑")

    if keyword == 'q':
        break






