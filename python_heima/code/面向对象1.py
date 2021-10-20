# 需求 小猫爱吃鱼 小猫爱喝水
class Cat():

    def __init__(self, name):
        # print("这是初始化方法，会自动调用。在这里可以设置属性的初始值")
        self.name = name

    def eat(self):
        print("%s 吃鱼" % self.name)

    def drink(self):
        print("喝水")

cat1 = Cat('一号猫')
cat1.eat()
cat1.drink()
