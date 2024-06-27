# -*- coding = utf-8 -*-
# @Time: 2024/5/31 15:18
# @Author: ZhouYanHui

# 静态方法:类可以直接调用,实例对象也可以调用,推荐类调用
# 类方法:类可以直接调用,实例对象也可以调用,推荐类调用
# 对象方法:实例对象调用,类不可调用


class Student:
    school = '一中'

    @staticmethod  # 静态方法,装饰器
    def open():
        print('开学了!')

    @classmethod  # 类方法,装饰器
    def close(cls):  # cls表示当前引用的类对象
        print(f'{cls.school}放假了')

    def init(self, age):  # 对象方法,self表示当前引用的实例对象
        self.age = age
        print(f'我{self.age}岁开始学习')


stu = Student()  # 实例化,创建实例对象 stu
# Student.open()  # 类调用静态方法,print('开学了')
# Student.close()  # 类调用类方法,一中放假了
# stu.open()  # 实例对象调用静态方法,开学了
# stu.close()  # 实例对象调用类方法,一中放假了

# print(stu.age)  # 报错(stu 没有 age 实例变量)
stu.init(7)  # 实例对象调用对象方法 init() 我7岁开始学习
print(stu.age)  # 7,不报错
