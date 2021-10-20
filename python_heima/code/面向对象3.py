'''
房屋和家具
'''

# 家具类
class HouseItem:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "%s占地面积%.2f" %(self.name, self.area)


# 房子类
class House:
    def __init__(self, type, area):
        self.type = type
        self.area = area
        self.free_area = self.area
        self.item_list = []

    def add_item(self, item):
        if item.area > self.free_area:
            print('家具太大，不能放入房间')
            return 0
        self.free_area -= item.area
        self.item_list.append(item.name)
        print('房子添加家具-%s, 房间剩余面积 %.2f' % (item.name, self.free_area))


    # 这个类的描述性方法
    def __str__(self):
        return  str(self.item_list)


bed = HouseItem('席梦思', 4)
chest = HouseItem('衣柜', 2)
table = HouseItem('桌子', 1.5)


h1 = House('三室一厅', 90)
h1.add_item(bed)
h1.add_item(table)
h1.add_item(chest)
print(h1)


