'''
士兵许三多有一把AK47
士兵可以开火
枪能发射子弹
枪装填子弹
'''

# 枪类
class Gun:
    def __init__(self, model):
        self.model = model
        self.bullte_count = 0

    def add_bullte(self, count):
        self.bullte_count += count

    def shoot(self):
        if self.bullte_count <= 0:
            print('%s没有子弹了' %self.model)
            return
        self.bullte_count -= 1
        print('射击了一枪, 剩余子弹数量: %d' % (self.bullte_count))

# 士兵类
class Soldier:
    def __init__(self, name):
        self.name = name
        self.gun = None

    def fire(self):
        # 开火
        if self.gun is None:
            print("%s 还没有枪" % self.name)
            return

        self.gun.add_bullte(50)
        self.gun.shoot()
        print("%s射中了敌人" % self.name)



AK47 = Gun('AK47')


xusanduo = Soldier('许三多')
# print(xusanduo.gun)
xusanduo.gun = AK47
# print(xusanduo.gun)
xusanduo.fire()

