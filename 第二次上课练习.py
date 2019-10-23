# 1、打印小猫爱吃鱼，小猫要喝水
class Cat:
    def eat(self, food):
        print('小猫爱吃{}'.format(food))

    def drink(self):
        print('小猫要喝水')


catty = Cat()
catty.eat('鱼')
catty.drink()
# 2、小明爱跑步，爱吃东西。——有吃、跑步两种方法
# 1）小明体重75.0公斤  ——人的属性
# 2）每次跑步会减肥0.5公斤  ——跑步的方法，每次减肥0.5公斤
# 3）每次吃东西体重会增加1公斤——吃的方法，每次吃增加1公斤
# 4）小美的体重是45.0公斤—— 小美的属性


class Person:
    def __init__(self, weight, name):
        self.weight = weight
        self.name = name

    def run(self):
        self.weight -= 0.5

    def eat(self):
        self.weight += 1.0


xiaoming = Person(75.0, '小明')
xiaomei = Person(45.0, '小美')
xiaoming.run()
xiaomei.eat()
xiaomei.run()
print('{}现在的体重是{}'.format(xiaoming.name, xiaoming.weight))
print('{}现在的体重是{}'.format(xiaomei.name, xiaomei.weight))
# 3、摆放家具
# 需求：
# 1）.房子有户型，总面积和家具名称列表（用字典更直接一点？）
#    新房子没有任何的家具
# 2）.家具有名字和占地面积，其中
#    床：占4平米
#    衣柜：占2平面
#    餐桌：占1.5平米
# 3）.将以上三件家具添加到房子中
# 4）.打印房子时，要求输出:户型，总面积，剩余面积，家具名称列表


class Room:
    def __init__(self, room_type, area, furniture):
        self.room_type = room_type
        self.area = area
        self.furniture = furniture

    def room(self):
        sum = 0
        for i in list(self.furniture.values()):
            sum += i
        print('户型是{}，总面积{}，剩余面积有{}，家具有{}'
              .format(self.room_type, self.area, self.area - sum, list(self.furniture.keys())))


dic = {}
dic1 = {'床': 4, '衣柜': 2, '餐桌': 1.5}
new_room = Room('三室一厅', 90.26, dic)
new_room.room()

room = Room('三室一厅', 90.26, dic1)
room.room()

# 定义Room1 和 Furniture 两个类来实现
# Room 有户型，总面积和家具名称属性
# Furniture 有名字和占地面积 属性
# Room1类中调用Furniture中的属性进行打印


class Furniture:
    def __init__(self, name, furniture_area):
        self.name = name
        self.furniture_area = furniture_area


class Room1:
    def __init__(self, room_type1, area_total, furniture_name=[]):
        self.room_type1 = room_type1
        self.area_total = area_total
        self.furniture_name = furniture_name
        self.area_left = area_total

    def add_furniture(self, jiaju):
        self.furniture_name.append(jiaju.name)
        # area_left = self.area_total
        self.area_left -= jiaju.furniture_area

    def room_print(self):
        print('户型{}总面积{}家具有{}剩余面积{}'.format(self.room_type1, self.area_total, self.furniture_name, self.area_left))


bed = Furniture('床', 4)
closet = Furniture('衣柜', 2)
table = Furniture('餐桌', 1.5)
room1 = Room1('三室一厅', 30)
room1.add_furniture(bed)
room1.add_furniture(closet)
room1.add_furniture(table)
room1.room_print()


# 4.士兵开枪
# 需求：
# 1）.士兵瑞恩有一把AK47
# 2）.士兵可以开火(士兵开火扣动的是扳机)
# 3）.枪 能够 发射子弹(把子弹发射出去)
# 4）.枪 能够 装填子弹 --增加子弹的数量

# 士兵：姓名  枪  开火（使用枪）
# 枪：型号 子弹数量 发射动作   装填子弹


class Gun:
    def __init__(self, gun_name, bullet_count=30):
        self.gun_name = gun_name
        self.bullet_count = bullet_count

    def fire(self):
        if self.bullet_count > 0:
            print('发射一发子弹')
            self.bullet_count -= 1
            print('子弹还剩{}'.format(self.bullet_count))
        else:
            print('重新装弹')
            self.reload()

    def reload(self):
        self.bullet_count += 30
        print('子弹重新装填，{}发'.format(self.bullet_count))


class Soldier:
    def __init__(self, soldier_name, gun_soldier):
        self.soldier_name = soldier_name
        self.gun_soldier = gun_soldier
        print('士兵{}有一把{}'.format(self.soldier_name, self.gun_soldier))

    def shoot(self, bullet_carry):
        Gun(self.gun_soldier, bullet_carry).fire()


ryen = Soldier('瑞恩', 'AK47')
ryen.shoot(10)


# 读取文件内容
with open(r'E:\code\test.txt', 'r') as test:
    # 定义列表存放L开头的姓名
    l = []
    # 定义列表存放出生日期
    age = []
    # 定义列表存放女性信息
    female = []
    s = test.readlines()
    print(s)
    for i in s:
        print(i)
        if i.find('L') != -1:
            l.append(i.split('|')[0])
        age.append(i.split('|')[-1].strip())
        if i.find('女') != -1:
            female.append(i.strip())
    # for line in test:
    #     # line.strip()
    #     str3 = line.strip().split('|')
    #     if line.find('l') != -1:
    #         l.append(str3[0])
    #     age.append(age.append(str3[-1]))
    print(l)
    print(sorted(age))
    print(female)
    # for line in test:
    #     # line.strip()
    #     str3 = line.strip().split('|')
    #     if line.find('l') != -1:
    #         l.append(str3[0])
    #     age.append(age.append(str3[-1]))
    # print(L)

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
# 任务1-找出所有L开头的人名
# 任务2-按照年龄进行排序
# 任务3-找出所有女性用户的信息
f = open(r'E:\code\data1.txt', 'r')
s = f.readlines()
# print(s)
f.close()
s1 = []
for i in s:
    s1.append(i.strip().split('|'))
for j in range(len(s1) - 1):
    for i in range(len(s1) - 1):
        if s1[i][-1] > s1[i + 1][-1]:
            c = s1[i]
            s1[i] = s1[i + 1]
            s1[i + 1] = c
s2 = []
for i in s1:
    s2.append('|'.join(i))
print('按年龄从大到小排列{}'.format(s2))
s3 = []
s4 = []
for i in s:
    if '女' in i:
        s3.append(i.strip())
    if i.startswith('L'):
        s4.append(i.strip())
print('女性信息{}'.format(s3))
print('姓名中带L人员信息{}'.format(s4))
