# class Person():
#     #__init__方法默认执行
#     def __init__(self,name,sex):
#         self.name = name
#         self.sex = sex
#
#     def eat(self,food):
#         print('{}吃{}'.format(self.name,food))
#     def sleep(self):
#         print('睡觉')
#
# #实例化
# a = Person('姚','female')
# #调用类中的方法
# a.eat('wasabi')
# a.sleep()
#
# class Student():
#     def __init__(self,name):
#         self.name = name
#
#     def study(self,kecheng):
#         print('{}学习{}课程'.format(self.name,kecheng))
#
# ss = Student('Tom')
# ss.study('数学')
#
# class Student():
#     def __init__(self,sno):
#         self.sno = sno
#
#     def study(self,class_name):
#         print('学号为{}的学生，学习{}课程'.format(self.sno,class_name))
#
# Tony = Student(10)
# Tony.study('高数')


class Person():
    #__init__方法默认执行
     def __init__(self,name,sex):
         self.name = name
         self.sex = sex

     def eat(self, food):
         print('{}吃{}'.format(self.name, food))

     def sleep(self):
         print('睡觉')


class Teacher(Person):
    def __init__(self, gh, name, sex):
        Person.__init__(self, name, sex)
        self.gh = gh

    def teach(self, class_name, work_place, salary):
        print('gh为{}的老师，教{}课'.format(self.gh, class_name))
        print('gh为{}老师，在{}上班，一月工资{}'.format(self.gh, work_place, salary))
        print('名字是{}，工号为{}的老师，吃饭'.format(self.name, self.gh))


t = Teacher('10', 'Ms.Wang', 'female')
t.teach('数学', '教室', '1000')


# class Animal:
#     def __init__(self,color):
#         self.color = color
#
#     def eat(self):
#         print('吃东西')
#     def drink(self):
#         print('喝东西')
#
# class Dog(Animal):
#     def __init__(self,color,size):
#         Animal.__init__(self,color)
#         self.size = size
#
#     def bark(self):
#         print('{}{}的汪 汪汪叫'.format(self.color,self.size))
#
# dogy = Dog('黄','大')
# dogy.eat()
# dogy.bark()
# dogy.drink()


