# -*- coding: utf-8 -*-
# @Time: 2024/6/27 14:56
# @Auth: Zhou Yanhui


class Person:

    def __init__(self, name, age):
        self.__name = name  # 私有属性
        if age <= 0:
            self.__age = '年龄必须大于0'  # 私有属性
        else:
            self.__age = age  # 私有属性

    # 利用公有方法访问私有属性
    def show_info(self):
        print(f'姓名: {self.__name}')
        print(f'年龄: {self.__age}')

    # 私有方法
    def __sleep(self):
        print('我要睡觉,晚安!')

    # 利用公有方法调用私有方法
    def sleep(self):
        self.__sleep()


p = Person('赵六', 26)

# print(p.__name)  # 报错
# print(p.__age)  # 报错
# p.show_info()  # 姓名: 赵六 年龄: 26

# p.__sleep()  # 报错
# p.sleep()  # 我要睡觉,晚安!
