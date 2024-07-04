# -*- coding: utf-8 -*-
# @Time: 2024/7/2 10:53
# @Auth: Zhou Yanhui


# __init__(self[,...])  初始化方法,在实例化过程中被调用
# class EX:
#     def __init__(self, arg1, arg2):
#         print(f'__init__被调用, arg1: {arg1}, arg2: {arg2}')
#
#
# EX('a', 'b')  # __init__被调用, arg1: a, arg2: b


# __call__(self[,...])  当实例对象像函数那样被 调用 时,会调用该方法
# class EX:
#     def __call__(self, arg1, arg2):
#         print(f'__call__被调用, arg1: {arg1}, arg2: {arg2}')
#
#
# e = EX()  # 实例化的时候不会调用 __call__ 方法
# e('a', 'b')  # __call__被调用, arg1: a, arg2: b


# __getitem__(self, key)  当执行 self[key] 操作时, 会调用该方法
# class Ex:
#     def __getitem__(self, key):
#         print(f'__getitem__被调用, key:{key}')
#         print(['a', 'b', 'c'][key])
#         print({0: '零', 1: '壹', 2: '贰'}[key])
#
#
# e = Ex()
# e[2]


# __len__(self)  对实例对象求长度时, 会调用该方法, 要求必须返回整数类型
# class EX:
#     def __len__(self):
#         return 1234
#
#
# e = EX()
# print(len(e))


# __repr__(self) / __str__(self)  实例对象转字符串时, 会调用该方法, 要求必须返回字符串类型
# class EX:
#     def __repr__(self):
#         return '__repr__被调用'
#
#     def __str__(self):  # __str__优先被调用
#         return '__str__被调用'
#
#
# e = EX()
# print(str(e))
# print(f'{e}')
# print(e)
