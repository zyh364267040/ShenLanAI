# -*- coding: utf-8 -*-
# @Time: 2024/6/27 16:05
# @Auth: Zhou Yanhui


# 三个内容不同的change方法使用相同的名字命名
# 只要改变change的调用对象, 就可以调用不同内容的方法
class Apple:

    def change(self):
        return '我变成了苹果汁!'


class Banana:

    def change(self):
        return '我变成了香蕉汁!'


class Mango:

    def change(self):
        return '我变成了芒果汁!'


class Juicer:

    def work(self, fruit):
        print(fruit.change())


a = Apple()  # 实例化
b = Banana()
m = Mango()
j = Juicer()

j.work(a)  # 我变成了苹果汁!
j.work(b)  # 我变成了香蕉汁!
j.work(m)  # 我变成了芒果汁!
