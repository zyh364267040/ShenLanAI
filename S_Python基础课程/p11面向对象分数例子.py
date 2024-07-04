# -*- coding: utf-8 -*-
# @Time: 2024/7/4 11:04
# @Auth: Zhou Yanhui


# 分数运算案例
class Fraction:

    def __init__(self, a, b):
        if b == 0:
            raise ZeroDivisionError('分母不能为0')
        self.a = a
        self.b = b

    def __str__(self):
        # 获取两个参数的最大公约数
        gcd = self.get_gcd(self.a, self.b)

        a = self.a // gcd
        b = self.b // gcd

        if b < 0:
            a = -a
            b = -b
        if b == 1:
            return f'{a}'
        else:
            return f'{a}/{b}'

    # 加法
    def __add__(self, other):  # self: 左边  other: 右边
        other = self.num_to_frac(other)  # 调用函数, 实例化, 返回实例对象

        temp = Fraction(self.a * other.b + other.a * self.b, self.b * other.b)
        return temp  # 例如Fraction(12, 9)

    def __radd__(self, other):  # self: 右边, other: 左边
        other = self.num_to_frac(other)
        return self + other

    # 减法
    def __sub__(self, other):
        other = self.num_to_frac(other)
        return Fraction(self.a * other.b - other.a * self.b, self.b * other.b)

    def __rsub__(self, other):
        other = self.num_to_frac(other)
        return self - other

    # 乘法
    def __mul__(self, other):
        other = self.num_to_frac(other)
        return Fraction(self.a * other.a, self.b * other.b)

    def __rmul__(self, other):
        other = self.num_to_frac(other)
        return self * other

    # 除法
    def __truediv__(self, other):
        other = self.num_to_frac(other)
        return Fraction(self.a * other.b, self.b * other.a)

    def __rtruediv__(self, other):
        other = self.num_to_frac(other)
        return self / other

    @staticmethod
    def get_gcd(x, y):
        """
        求最大公约数
        """
        for i in range(min(abs(x), abs(y)), 0, -1):
            # 当i是最大公约数时, x % i == 0, y % i == 0, or左边为假, 返回右边0
            # not 0, 条件成立
            if not (x % i or y % i):
                return i
        else:
            return y  # 当x为0, 返回y

    @staticmethod
    def num_to_frac(obj):
        """
        数字转Fraction对象
        1. 分数
        2. 整数或bool值
        3. 浮点数
        """
        if type(obj) is Fraction:
            return obj
        elif isinstance(obj, int):  # int类是bool类的父类
            return Fraction(obj, 1)
        elif type(obj) is float:
            # 10的n次方, n等于小数点后面的位数
            p = 10 ** len(str(obj).split('.')[-1])
            return Fraction(int(obj * p), p)
        else:
            raise TypeError(f'不支持{type(obj)}的数据')


f1 = Fraction(6, 8)
# print(f1)
# print(f1 + 0.5)
# print(0.5 + f1)
# print(f1 - 0.5)
# print(0.5 - f1)
# print(f1 * 0.5)
# print(0.5 * f1)
print(f1 / 0.5)
print(0.5 / f1)
