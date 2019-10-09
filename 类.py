#定义一个学生类：Student、内部含有一个方法：study，实现打印：xx学习xx课程
class Student():
    #定义一个类方法实现打印
    def study(self,name,lesson):
        print("{}学习{}课程".format(name,lesson))

a = Student().study('小明','英语')
print(dir(Student))

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

print(a.__class__)
print(isinstance(a,a.__class__))

print(Person.__dict__)
print(tom.__dict__)