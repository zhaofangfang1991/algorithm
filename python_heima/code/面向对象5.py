'''
多态：不同的子类对象调用相同的父类方法，产生不同的执行结果
'''

class Dog(object):
    def __init__(self, name):
        self.name = name
    def game(self):
        print("%s在快乐的玩耍" % self.name)


class XiaoTianDog(Dog):
    def game(self):
        print("%s在天空中飞翔着玩耍" %self.name)


class Person(object):
    def __init__(self, name):
        self.name = name

    def play_with_dog(self, dog):
        print("%s在逗%s" % (self.name, dog.name))
        dog.game()


wangcai = Dog('旺财')
xiaotianquan = XiaoTianDog('哮天犬')

xiaoming = Person('小明')
xiaoming.play_with_dog(wangcai)
xiaoming.play_with_dog(xiaotianquan)

