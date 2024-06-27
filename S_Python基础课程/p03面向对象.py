# -*- coding = utf-8 -*-
# @Time: 2024/5/30 22:27
# @Author: ZhouYanHui


class Student:
    school = '二中'  # 类变量

    def __init__(self, name):
        self.name = name  # 实例变量


stu1 = Student('小明')  # 实例化,得到实例对象stu1
stu2 = Student('小红')  # 实例化,得到实例对象stu2

# print(stu1.name)  # 小明,实例对象stu1  引用实例变量
# print(stu2.name)  # 小红

# print(Student.school)  # 二中,类对象引用类变量(推荐)
# print(stu1.school)  # 二中,实例对象stu1 引用类变量
# print(stu2.school)  # 二中

stu1.name = '小强'  # 把实例对象 sut1.name 变量指向新的值
# print(stu1.name)  # 小强
# print(stu2.name)  # 小红

# 类变量是公有的
Student.school = '一中'  # 把 student 的类变量的值改了
# print(Student.school)  # 一中
# print(stu1.school)  # 一中
# print(stu2.school)  # 一中

# stu1.school = '三中'  # 动态定义实例变量
# print(stu1.school)  # 三中,实例对象 stu1 的实例变量 school 值改了
# print(Student.school)  # 一中 类变量的值保持不变
# print(stu2.school)  # 一中