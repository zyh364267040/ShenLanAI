# -*- coding: utf-8 -*-
# @Time: 2024/6/27 15:31
# @Auth: Zhou Yanhui


# 所有的类都默认继承object, 只是一般不用写出来
# 子类继承父类后, 会拥有父类中所有的非私有属性和方法
# 继承的作用: 从子类来看, 继承可以简化代码; 从父类来看, 子类是对父类功能的扩充


# 单继承
# class Person:
#     state = 'China'

    # def eat(self):
    #     print('吃饭')

    # def speak(self):
    #     print('说话')


# class Student(Person):
#     def study(self):
#         print('读书')


# class Worker(Person):

    # def work(self):
    #     print('搬砖')


# stu = Student()  # 实例化
# print(Student.state)  # 子类引用父类的属性, China
# stu.study()  # 子类调用自己的方法, 读书
# stu.eat()  # 子类调用父亲的方法, 吃饭
# stu.speak()  # 说话

# wk = Worker()  # 实例化
# print(Worker.state)  # China
# wk.work()  # 搬砖
# wk.eat()  # 吃饭
# wk.speak()  # 说话


# class Animal:

    # def eat(self):
    #     print('吃东西')


# class Cat(Animal):
#     def catch_mouse(self):
#         print('抓老鼠')


# class Ragdoll(Cat):  # 布偶猫
#     def cute(self):
#         print('卖萌')


# c1 = Ragdoll()  # 实例化
# c1.cute()  # 子类调用自己的方法, 卖萌
# c1.catch_mouse()  # 子类调用父类的方法, 抓老鼠
# c1.eat()  # 调用父类的父类的方法, 吃东西


# class A:
#     a = 1

    # def pr(self):
    #     print('A')


# class B(A):
#     def pr(self):
#         print('B')


# class C(B):
#     a = 3

    # def pr(self):
    #     print('C')


# class D(B):
#     pass


# c = C()  # 实例化,返回实例对象
# c.pr()  # C
# print(c.a)  # 3

# d = D()  # 实例化
# d.pr()  # B
# print(d.a)  # 1

# 多继承
# class Biology:

    # def eat(self):
    #     print('Biology吃东西')


# class Animal:

    # def sleep(self):
    #     print('Animal睡觉')

    # def cute(self):
    #     print('Animal卖萌')


# class Cat:

    # def sleep(self):
    #     print('Cat睡觉')


# class Ragdoll(Cat, Animal, Biology):
#     pass


# rd = Ragdoll()  #
# rd.eat()  # Biology吃东西
# rd.sleep()  # Cat睡觉
# rd.cute()  # Animal卖萌


# 方法重写
# class Animal:

    # def __init__(self, food):
    #     self.food = food

    # def eat(self):
    #     print(f'动物吃{self.food}')


# class Cat(Animal):

    # def eat(self):
    #     print(f'猫吃{self.food}')


# c = Cat('鱼')  # 实例化,调用父类的初始化方法
# c.eat()  # 猫吃鱼


# super()
# class Animal:

    # def eat(self):
    #     print('吃东西')


# class Cat(Animal):

    # def eat(self):
    #     print('吃鱼')


# class Ragdoll(Cat):

    # def eat(self):
    #     print('喝咖啡')


# rd = Ragdoll()  # 实例化
# rd.eat()  # rd调用Ragdoll类中的对象方法, 喝咖啡
# super(Ragdoll, rd).eat()  # rd调用Ragdoll父类的方法, 吃鱼
# super(Cat, rd).eat()  # rd调用Ragdoll父类的方法, 吃东西
# Animal.eat(rd)  # rd调用Animal类的对象方法, 吃东西

# c = Cat()  # 实例化
# c.eat()  # c调用Cat类中的对象方法, 吃鱼
# super(Cat, c).eat()  # c调用Cat父类的对象方法, 吃东西


# class A:

    # def __init__(self, name):
    #     self.name = name
    #     self.Q()

    # def E(self):
    #     print('E方法被调用')

    # def Q(self):
    #     print(self.name, 'Q方法被调用')


# class B(A):
#     pass


# b = B('张三')  # 实例化, 张三 Q方法被调用
# b.E()  # 调用父类的E方法, E方法被调用
# b.Q()  # 调用父类的Q方法, 张三 Q方法被调用


# class C(A):
#
#     def __init__(self, name):
#         self.names = name
#         super(C, self).__init__(name)


# c = C('赵六')  # 实例化, 优先调用C中的初始化方法
# super(C, c).__init__('赵六')
# c.Q()


# class D(A):
#
#     def __init__(self, name):
#         super(D, self).__init__('李四')
#         self.name = name  # 王五


# d = D('王五')  # 实例化, 李四 Q方法被调用
# d.Q()  # 王五 Q方法被调用


# class A:
#
#     var1 = 123
#
#     @classmethod
#     def func1(cls):
#         print(cls.var1)
#
#     @staticmethod
#     def func2():
#         print(A.var1)
#
#
# class B(A):
#     var1 = 321
#
#
# A.func1()  # 123
# A.func2()  # 123
# B.func1()  # 321
# B.func2()  # 123


# class Person:
#
#     school = '引用school成功'  # 私有属性
#
#     def __sleep(self):  # 私有方法
#         print('调用__sleep成功')
#
#     def sleep(self):  # 非私有方法
#         print('调用sleep成功')
#
#
# class Student(Person):
#     pass
#
#
# stu = Student()
# print(stu.school)  # 子类继承父类的非私有属性, 引用school成功
# stu.sleep()  # 子类继承父类的非私有方法, 调用sleep成功
#
# print(stu.__school)  # 报错
# stu.__sleep()  # 报错, 子类不能调用父类的私有属性和私有方法


# class Person:
#
#     def __init__(self):
#         self.__func()  # 可以调用
#
#     def __func(self):
#         print(1234)
#
#
# class Student(Person):
#     pass
#
#
# stu1 = Student()  # 实例化, 1234
# stu1.__func()  # 调用不到


# class A:
#     pass


# class B(A):
#     pass
#
#
# class C(A):
#     pass


# a = A()  # 实例化
# b = B()
# c = C()
# 判断 a 是不是 A 的实例对象
# print(isinstance(a, A))  # True
# print(type(a) is A)  # Ture
# print(isinstance(b, A))  # True, 考虑继承
# print(type(b) is A)  # False, type不考虑继承
# print(isinstance(c, A))  # True
# print(type(c) is A)  # False
# print(isinstance(c, (B, A)))  # True


class A:
    pass


class B(A):
    pass


class C(A):
    pass


print(issubclass(B, A))  # B是不是A的子类, True
print(issubclass(C, A))  # True
print(issubclass(A, A))  # True
print(issubclass(C, (B, A)))  # True

