'''
小明 爱跑步，爱吃东西
跑步体重减少0.5公斤
吃东西体重增加1公斤
'''

class Person:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def eat(self):
        self.weight += 1
        print("%s吃东西后，的体重是%.2f" %(self.name, self.weight))


xiaoming = Person('小明', 75)
xiaoming.eat()

xiaomei = Person('小美', 50)
xiaomei.eat()
