# -*- coding: utf-8 -*-
# @Time: 2024/6/26 17:19
# @Auth: Zhou Yanhui


class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f'名字: {self.name}, 年龄: {self.age}, 地址: {self.address}')

    def study1(self):
        self.course = '语文'
        print(f'今天学习的科目是: {self.course}')

    def study2(self):
        print(f'今天学习的科目是: {self.course}')


stu1 = Student('张三', 18)  # 实例化
stu2 = Student('小明', 28)

# stu1.show_info()  # 报错
stu1.address = '黄土高坡'  # stu1 动态定义实例变量
# print(stu1.address)  # 黄土高坡
# stu1.show_info()

# print(stu2.address)  # 报错
# stu2.study2()  # 报错
stu2.study1()  # 今天学习的科目是: 语文
# stu2.study2()  # 今天学习的科目是: 语文

stu2.course = '数学'
stu2.study1()  # 今天学习的科目是: 语文


class Worker:

    def __init__(self, name):
        self.name = name


wk = Worker('李四')  # 实例化
Worker.factory = '江南皮革厂'  # 动态定义类变量
# print(Worker.factory)  # 类对象引用类变量(推荐), 江南皮革厂
# print(wk.factory)  # 实例对象引用类变量, 不推荐, 江南皮革厂

# print(Worker.name)  # 报错
Worker.name = '王五'  # 动态定义类变量(在实际种要避免名字冲突)
# print(Worker.name)  # 类对象引用类变量, 王五
print(wk.name)  # 李四


class Person:
    eat = 'rice'

    def __init__(self, age):
        self.age = age


p = Person(18)  # 实例化
# print(Person.eat)  # rice

# delattr(Person, 'eat')  # 删除类属性, eat
# del Person.eat  # 等价于上一行
# print(Person.eat)  # 报错

# print(p.age)  # 18, 实例变量(实例属性)
# del p.eat
# delattr(p, 'age')  # 删除实例属性age
# print(p.age)  # 报错

# print(getattr(Person, 'eat'))  # rice
# print(Person.eat)  # 等价于上一行, rice

# print(getattr(p, 'age'))  # 18
# print(p.age)  # 等价于上一行
#
# print(getattr(Person, 'height', 178))  # 178
# print(getattr(Person, 'height'))  # 报错, 这个方法调用没有这个属性的函数时, 如果给了默认值会嗲用默认值, 如果没有回报错

# print(hasattr(Person, 'eat'))  # True, 通过调用getattr实现判断属性是否存在
# print(hasattr(p, 'eat'))  # True
# print(hasattr(p, 'age'))  # True
# print(hasattr(p, 'height'))  # False

setattr(Person, 'eat', '面条')  # 对已有属性进行修改
print(Person.eat)  # 面条

setattr(Person, 'drink', '水')  # 没有的属性会增加
print(Person.drink)  # 水

setattr(p, 'age', 29)  # 修改实例对象属性
print(p.age)  # 29

setattr(p, 'height', 178)  # 新增实例对象属性
print(p.height)  # 178

