# -*- coding = utf-8 -*-
# @Time: 2024/5/22 17:07
# @Author: ZhouYanHui

# result = filter(lambda x: x-1, [1, 2, 0, False, 4])
# print(result)
# print(list(result))

# result = map(lambda x: x**2, [1, 2, 3])
# print(list(result))
#
# result = map(lambda x, y, z: x+y+z, [1, 2, 3], [4, 5, 6], [7, 8, 9])
# print(list(result))

from functools import reduce


# def add(m, n):
#     s = m + n
#     return s
# 第一步 1+2
# 第二步 (1+2)+3
# 第三步 [(1+2)+3]+4
# result = reduce(add, [1, 2, 3, 4])
# print(result)

# result = reduce(lambda x, y: 2 * x + y, [1, 2, 3], 5)
# print(result)

# def func(n):
#     n0 = 1
#     n1 = 1
#     print(f'n0: {n0}\t n1: {n1}\t n0+n1: {n0+n1}\t')
#     for _ in range(n):
#         print(f'n0: {n0}\t n1: {n1}\t n0+n1: {n0 + n1}\t')
#         n0, n1 = n1, n0 + n1
#
#     return n0
#
# for i in range(10):
#     print(f'第{i}个月的兔子数量:{func(i)}')


def get_rabbits(n):
    if n < 2:
        return 1

    return get_rabbits(n-1) + get_rabbits(n-2)


print(get_rabbits(9))
