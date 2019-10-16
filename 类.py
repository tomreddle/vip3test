#定义一个学生类：Student、内部含有一个方法：study，实现打印：xx学习xx课程
class Student:
    #定义一个类方法实现打印
    def study(self,name,lesson):
        print("{}学习{}课程".format(name,lesson))

a = Student()#.study('小明','英语')
a.study('小明','英语')
#print(dir(Student))

#定义一个类名：Student—学生、类内部含有一个属性：sno—学号，
# 一个方法：study—学习，实现打印：学号为xx的学生，学习xx课程
class Student():
    sno = 0
    def study(self,lesson):
        print( "学号为%d的学生，学习%s课程"%(self.sno , lesson) )

a = Student()
print(a.study)
a.sno = 10
a.study("math")



#使用初始化进行参数赋值
class Person:
    def __init__(self,name):
        self.name = name

    def eat(self,food):
        print(self.name + "喜欢吃" + food )

tom = Person('Tom')
#tom.name = "汤姆"
tom.eat("鱼")

# print(a.__class__)
# print(isinstance(a,a.__class__))
#
# print(Person.__dict__)
# print(tom.__dict__)

class Gun():
	# 初始化
    def __init__(self,model):
        self.model = model
        self.bullet_count = 0
    # 规范化
    def __str__(self):
        return '%s有%d发子弹' %(self.model,self.bullet_count)
    # 定义方法
    def shoot(self):
        if self.bullet_count > 0:
            print('发射子弹....')
            self.bullet_count -= 1
        else:
            print('枪内无子弹，无法发射....')
    def add_bullet(self,count):
        self.bullet_count += count
        print('装填子弹:%s颗....' %count)

# 定义士兵类
class Soldier():
    # 初始化
    def __init__(self,name):
        self.name = name
        self.Gun = None
    # 定义方法（关联枪类）
    def fire(self):
        if self.Gun == None:
            print('%s还没有枪...' %self.name)
        else:
            self.Gun.add_bullet(10)
            print('开火....')
            self.Gun.shoot()

# 创建枪对象
AK47=Gun('AK47')
print(AK47)
#调用方法

AK47.add_bullet(10)
AK47.shoot()
print(AK47)

# 创建士兵对象
瑞恩=Soldier('瑞恩')
# 调用方法
瑞恩.fire()
瑞恩.Gun = AK47
瑞恩.fire()
print(AK47)
