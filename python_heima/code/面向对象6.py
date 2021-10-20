'''
类属性：最高分
类方法：显示最高分
对象属性：玩家姓名
对象方法：开始游戏
静态方法：显示游戏说明
'''

class Game(object):
    top_score = 100

    @classmethod
    def show_top_score(cls):
        print("该游戏截至目前最高分为%d" % cls.top_score)

    @staticmethod
    def show_rule():
        print("这里是静态方法，显示游戏说明")

    def __init__(self, name):
        self.name = name

    def start_game(self):
        print("%s开始游戏了" % self.name)

print(Game.top_score)
Game.show_rule()

wanjia1 = Game('小明')
wanjia1.start_game()



