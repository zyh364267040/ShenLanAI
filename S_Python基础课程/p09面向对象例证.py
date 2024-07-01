# -*- coding: utf-8 -*-
# @Time: 2024/7/1 15:26
# @Auth: Zhou Yanhui


# 学生类
# class Student:
#     count = 0
#
#     def __init__(self, name, age, address):
#         self.name = name
#         self.age = age
#         self.address = address
#         self.show_time()
#         Student.count += 1
#
#     def show_time(self):
#         print(f'大家好! 我是{self.name}, 今年{self.age}岁, 家住在{self.address}, 欢迎大家有空来找我玩!')
#
#     def get_up(self):
#         print(f'{self.name}起床')
#
#     def wash(self):
#         print(f'{self.name}刷牙')
#         print(f'{self.name}洗脸')
#
#     def eat(self):
#         print(f'{self.name}吃菜')
#         print(f'{self.name}扒饭')
#
#     def login_in(self):
#         print(f'{self.name}账号登录成功')
#
#     def study(self):
#         print(f'{self.name}看视频')
#         print(f'{self.name}写代码')
#
#     def sleep(self):
#         print(f'{self.name}睡觉')
#
#     @classmethod
#     def counter(cls):
#         print(f'当前统计的学生人数是{cls.count}人')
#
#
# stu1 = Student('张三', 18, '黄土高坡')
# stu1.get_up()
# stu1.wash()
# stu1.eat()
# stu1.login_in()
# stu1.study()
# stu1.eat()
# stu1.study()
# stu1.eat()
# stu1.wash()
# stu1.sleep()
# Student.counter()
#
#
# # 老师类
# class Teacher:
#     count = 0
#
#     def __init__(self, name, age, address):
#         self.name = name
#         self.age = age
#         self.address = address
#         self.show_time()
#         Teacher.count += 1
#
#     def show_time(self):
#         print(f'大家好! 我是{self.name}, 今年{self.age}岁, 家住在{self.address}, 欢迎大家有空来找我玩!')
#
#     def get_up(self):
#         print(f"{self.name}起床")
#
#     def wash(self):
#         print(f"{self.name}刷牙")
#         print(f"{self.name}洗脸")
#
#     def eat(self):
#         print(f"{self.name}吃菜")
#         print(f"{self.name}扒饭")
#
#     def clock_in(self):
#         print(f"{self.name}今日打卡成功")
#
#     def work(self):
#         print(f"{self.name}授课")
#         print(f"{self.name}答疑")
#         print(f"{self.name}写代码")
#
#     def sleep(self):
#         print(f"{self.name}睡觉")
#
#     @classmethod
#     def counter(cls):
#         print(f"当前统计的老师人数是: {cls.count} 人")
#
#
# teacher1 = Teacher('老王', 40, '人民广场')
# teacher1.get_up()
# teacher1.wash()
# teacher1.eat()
# teacher1.clock_in()
# teacher1.work()
# teacher1.eat()
# teacher1.work()
# teacher1.eat()
# teacher1.wash()
# teacher1.sleep()
# Teacher.counter()


# 先创建人类, 老师和学生继承人类
class Person:

    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
        self.show_time()

    def show_time(self):
        print(f'大家好! 我是{self.name}, 今年{self.age}岁, 家住在{self.address}, 欢迎大家有空来玩哦!')

    def get_up(self):
        print(f'{self.name}起床')

    def wash(self):
        print(f'{self.name}刷牙')
        print(f'{self.name}洗脸')

    def eat(self):
        print(f'{self.name}吃菜')
        print(f'{self.name}扒饭')

    def sleep(self):
        print(f'{self.name}睡觉')


class Student(Person):
    count = 0

    def __init__(self, name, age, address, classes):
        self.classes = classes
        super().__init__(name, age, address)
        Student.count += 1

    def login_in(self):
        print(f'{self.name}登录账号成功')

    def study(self):
        print(f'{self.name}看视频')
        print(f'{self.name}写代码')

    @classmethod
    def counter(cls):
        print(f'当前统计的学生人数是:{cls.count}人')


class Teacher(Person):
    count = 0

    def __init__(self, name, age, address, department):
        self.department = department
        super().__init__(name, age, address)
        Teacher.count += 1

    def clock_in(self):
        print(f'{self.name}今日打卡成功')

    def work(self):
        print(f'{self.name}授课')
        print(f'{self.name}答疑')
        print(f'{self.name}写代码')

    @classmethod
    def counter(cls):
        print(f'当前统计的老师人数是:{cls.count}人')


stu1 = Student('张三', 18, '黄土高坡', '高一三班')
Student.counter()

teacher1 = Teacher('老王', 40, '人民广场', '教育部')
teacher2 = Teacher('老李', 41, '黄埔江', '黄埔军校')
Teacher.counter()
