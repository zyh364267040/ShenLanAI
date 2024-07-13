# -*- coding: utf-8 -*-
# @Time: 2024/7/8 17:03
# @Auth: Zhou Yanhui
import numpy as np
from typing import Iterable


# print(np.__version__)  # 1.26.4


# ndarray.ndim  秩,即轴的数量或维度的数量
# ndarray.shape  数组的形状
# ndarray.size  数组元素的总个数
# ndarray.dtype  ndarray对象的元素类型
# ndarray.itemsize  ndarray对象中每个元素的大小, 以字节为单位
# arr1 = np.array([1, 2, 3])
# print(arr1)  # [1 2 3]
# print(type(arr1))  # <class 'numpy.ndarray'>
# print(isinstance(arr1, np.ndarray))  # True
# print(isinstance(arr1, Iterable))  # True

# print(arr1.ndim)  # 1
# print(arr1.shape)  # (3,)
# print(arr1.size)  # 3
# print(arr1.dtype)  # int64
# print(arr1.itemsize)  # 8


# arr2 = np.array([[1, 2, 3], [4, 5, 2147483648]])
# print(arr2)
# print(arr2.ndim)  # 2
# print(arr2.shape)  # (2, 3)
# print(arr2.size)  # 6
# print(arr2.dtype)  # int64
# print(arr2.itemsize)  # 8


# arr3 = np.array([[[1, 2, 3], [4, 5, 6]],[[7, 8, 9], [10, 11, 12.]]])
# print(arr3)
# print(arr3.ndim)  # 3
# print(arr3.shape)  # (2, 2, 3)
# print(arr3.size)  # 12
# print(arr3.dtype)  # float64
# print(arr3.itemsize)  # 8


# arr4 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]], dtype=np.float32)
# print(arr4)
# print(arr4.ndim)  # 3
# print(arr4.shape)  # (2, 2, 3)
# print(arr4.size)  # 12
# print(arr4.dtype)  # float32
# print(arr4.itemsize)  # 4


# arr5 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12.]]], dtype=np.int32)
# print(arr5)
# print(arr5.ndim)  # 3
# print(arr5.shape)  # (2, 2, 3)
# print(arr5.size)  # 12
# print(arr5.dtype)  # int32
# print(arr5.itemsize)  # 4


# arr6 = np.array(13)
# print(arr6)  # 13
# print(arr6.ndim)  # 0
# print(arr6.shape)  # ()
# print(arr6.size)  # 1
# print(arr6.dtype)  # int64
# print(arr6.itemsize)  # 8


# np.asarray(a, dtype=None)  类似于np.array, 主要区别是当a是ndarray且dtype也匹配时, np.asarray不执行复制操作,
# 而np.array仍然会复制出一个副本,占用新的内存
# obj = [1, 2, 3]
# arr1 = np.array(obj)
# arr2 = np.asarray(obj)
# obj[1] = 4
# print(obj)  # [1, 4, 3]
# print(arr1)  # [1 2 3]
# print(arr2)  # [1 2 3]
#
# obj = np.array([1, 2, 3])
# arr1 = np.array(obj)
# arr2 = np.asarray(obj)
# obj[1] = 4
# print(obj)  # [1, 4, 3]
# print(arr1)  # [1 2 3]
# print(arr2)  # [1 4 3]

# asarray中的dtype和obj不匹配
# obj = np.array([1, 2, 3])
# arr1 = np.array(obj, dtype=np.float32)
# arr2 = np.asarray(obj, dtype=np.float32)
# obj[1] = 4
# print(obj)  # [1 4 3]
# print(arr1)  # [1. 2. 3.]
# print(arr2)  # [1. 2. 3.]


# np.copy(a)  a: array_like, 返回给定对象的数组副本
# a1 = [1, 2, 3]
# arr1 = np.array(a1)
# print(arr1)  # [1 2 3]
#
# a2 = np.array([1, 2, 3])
# arr2 = np.copy(a2)
# print(arr2)  # [1 2 3]


# ndarray.copy()  对象方法, 返回数组的副本
# arr = np.array([1, 2, 3])
# print(arr.copy())  # [1 2 3]


# np.empty(shape, dtype=np.float64)  返回给定形状和类型且未初始化的新数组
# print(np.empty((2, 3)))
# print(np.empty((2, 3), dtype=np.int32))


# np.empty_like(prototype, dtype=None)
# prototype: array_like
# dtype: 如果指定该参数, 将会覆盖结果的数据类型
# 返回形状和类型与给定prototype相同的新数组
# a = ([1, 2, 3], [4, 5, 6])
# print(np.empty_like(a))
#
# a = np.array([[1, 2, 3], [4, 5, 6.]])
# print(np.empty_like(a))
#
# a = np.array([[1, 2, 3], [4, 5, 6.]])
# print(np.empty_like(a, dtype=np.int32))


# np.zeros(shape, dtype=np.float64)  返回给定形状和类型的新数组, 并用零填充
# print(np.zeros((2, 3)))
# print(np.zeros((2, 3), dtype=np.int32))


# np.zeros_like(a, dtype=None)
# a: array_like
# dtype: 如果指定该参数, 将会覆盖结果的数据类型
# 返回一个与给定a具有相同形状和类型的零数组
# a = ([1, 2, 3], [4, 5, 6])
# print(np.zeros_like(a))
#
# a = ([1, 2, 3], [4, 5, 6.])
# print(np.zeros_like(a))
#
# a = ([1, 2, 3], [4, 5, 6.])
# print(np.zeros_like(a, dtype=np.int32))


# np.ones(shape, dtype=np.float64)  返回给定形状和类型的新数组, 并用1填充
# print(np.ones((2, 3)))
# print(np.ones((2, 3), dtype=np.int32))


# np.ones_like(a, dtype=None)
# a: array_like
# dtype: 如果指定该参数, 将会覆盖结果的数据类型
# 返回一个与给定a具有相同形状和类型的1构成的数组
# a = ([1, 2, 3], [4, 5, 6])
# print(np.ones_like(a))
#
# a = ([1, 2, 3], [4, 5, 6.])
# print(np.ones_like(a))
#
# a = ([1, 2, 3], [4, 5, 6.])
# print(np.ones_like(a, dtype=np.int32))


# np.full(shape, fall_value, dtype=None)  返回给定形状和类型的新数组, 并用full_value填充
# print(np.full((2, 3), 6))
# print(np.full((2, 3), 6.))
# print(np.full((2, 3), 6., dtype=np.int32))


# np.full_like(a, full_value, dtype=None)
# a: array_like
# dtype: 如果指定该参数, 将会覆盖结果的数据类型
# 返回一个与给定a具有相同形状和类型的full_value填充的数组
# a = ([1, 2, 3], [4, 5, 6])
# print(np.full_like(a, 6))

# 在没有指定dtype的情况下, 数据类型为a的数据类型
# a = np.array([[1, 2, 3], [4, 5, 6.]])
# print(np.full_like(a, 6.))
#
# a = np.array([[1, 2, 3], [4, 5, 6.]])
# print(np.full_like(a, 6., dtype=np.int32))


# np.eye(N, M=None, k=0, dtype=np.float64)
# N: 输出数组的行数
# M: 输出数组的列数, 如果为None, 则默认为N
# k: 对角线的索引, 默认为0, 表示主对角线, 正值表示上对角线, 负值表示下对角线
# dtype: 数组的数据类型
# 对角线为1, 其他地方为0(单位矩阵)
# print(np.eye(3))
# print(np.eye(3, 4))
# print(np.eye(3, 4, k=1))
# print(np.eye(3, 4, k=1, dtype=np.int32))


# np.identity(n, dtype=np.float64)  返回n*n的单位数组(主对角线为1, 其他元素为0的方形数组)
# print(np.identity(3))
# print(np.identity(3, dtype=np.int32))


# np.arange([star,]stop[,step], dtype=None)  返回给区间内的均匀间隔值构成的数组
# print(np.arange(3))  # [0 1 2]
# print(np.arange(3.0))  # [0. 1. 2.]
# print(np.arange(3, 7))  # [3 4 5 6]
# print(np.arange(3, 7, dtype=np.float64))  # [3. 4. 5. 6.]
# print(np.arange(3, 7, 2))  # [3 5]
# print(np.arange(7, 3, -2))  # [7 5]
# print(np.arange(3, 7, 0.5))  # [3.  3.5 4.  4.5 5.  5.5 6.  6.5]


# np.reshape(a, newshape)  保证size不变,在不更改数据的情况下位数组赋予新的形状
# newshape的一个形状唯独可以是-1, 值将自行推断
# arr1 = np.arange(6).reshape((2, 1, 3))
# arr2 = np.reshape(arr1, (6,))
# arr3 = np.reshape(arr1, (-1,))
# print(arr1)
# print(arr2)  # [0 1 2 3 4 5]
# print(arr3)  # [0 1 2 3 4 5]
#
# arr1 = np.arange(24)
# arr2 = np.reshape(arr1, (2, 2, -1, 2))
# print(arr2.shape)  # (2, 2, 3, 2)


# np.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)
# num: 生成的样本数量
# endpoint: 如果为True, stop为最后一个样本. 否则, 不包括在内
# retstep: 如果为True, 返回(samples, step), step是样本之间的间隔
# dtype: 如果没有给出dtype, 则从star和stop推断数据类型, 推断出的dtype永远不会是整数; 即使参数会产生一个整数数组, 也会选择np.float64
# 把给定区间分成num个均匀间隔的样本, 构成数组并返回(等差数列)
# print(np.linspace(1, 50))
# print(np.linspace(1, 10, num=10))  # [ 1.  2.  3.  4.  5.  6.  7.  8.  9. 10.]
# print(np.linspace(1, 10, num=10, endpoint=False))  # [1.  1.9 2.8 3.7 4.6 5.5 6.4 7.3 8.2 9.1]
# print(np.linspace(1, 10, num=10, retstep=True))  # (array([ 1.,  2.,  3.,  4.,  5.,  6.,  7.,  8.,  9., 10.]), 1.0)
# print(np.linspace(1, 10, num=10, dtype=np.int32))  # [ 1  2  3  4  5  6  7  8  9 10]


# np.logspace(start, stop, num=50, endpoint=True, base=10.0, dtype=None)
# star: 序列的起始值为: base ** star
# stop: 序列的终止值为: base ** stop
# num: 生成的样本数量
# endpoint: 如果为True, stop为最后一个样本, 否则, 不包括在内
# base: 对数log的底数
# dtype: 如果没有给出dtype, 则从start和stop推断数据类型. 推断出的dtype永远不会是整数; 即使参数会产生一个整数数组, 也会选择np.float64
# 把给定区间分成num个按对数尺度均匀间隔的样本, 构成数组并返回(等比数列)
# print(np.logspace(2.0, 3.0, num=4))  # [ 100.          215.443469    464.15888336 1000.        ]
# print(np.logspace(0, 9, 10, base=2))  # [  1.   2.   4.   8.  16.  32.  64. 128. 256. 512.]


# 算术和比较操作naarrays被定义为主元素操作
# a = np.array([[1, 2], [3, 4], [5, 6]])
# print(a + 2)
# print(a - 2)
# print(a * 2)
# print(a / 2)
# print(a < 4)
# print(a > 3)
#
# b = np.array([[2, 2], [2, 1], [1, 1]])
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a < b)
# print(a > b)


# 广播机制, 后缘维度相同或者不同的维度有1, 可以广播
# a = np.arange(24).reshape((2, 3, 4))
# b = np.arange(12).reshape((3, 4))
# c = np.arange(4).reshape((1, 4))
# d = np.arange(4).reshape(4)
# e = np.arange(12).reshape((1, 3, 4))
# f = np.arange(6).reshape((2, 3, 1))
# g = np.arange(2).reshape((2, 1, 1))
# h = np.arange(2).reshape((1, 2, 1, 1))
# i = np.arange(10).reshape((5, 2, 1, 1))
#
# print((a+b).shape)  # (2, 3, 4)
# print((a+c).shape)  # (2, 3, 4)
# print((a+d).shape)  # (2, 3, 4)
# print((a+e).shape)  # (2, 3, 4)
# print((a+f).shape)  # (2, 3, 4)
# print((a+g).shape)  # (2, 3, 4)
# print((a+h).shape)  # (1, 2, 3, 4)
# print((a+i).shape)  # (5, 2, 3, 4)


# 索引和切片
# 数组的索引和切片与Python中序列的索引和切片操作基本类似, 不同点在于:
# 1. 数组切片不会复制内部数组数据, 只会生成原始数据的新视图
# 2. 数组支持多维数组的多维索引和切片
# arr = np.arange(2, 10)
# print(arr)  # [2 3 4 5 6 7 8 9]
# item = arr[1]
# print(item)  # 3
# part = arr[-2: 1: -1]
# print(part)  # [8 7 6 5 4]
#
# arr[1] = 33  # 索引修改数组
# arr[3:] = [55, 66, 77, 88, 99]  # 切片修改数组
# print(item)  # 非视图, 3
# print(part)  # 新视图, [88 77 66 55  4]

# lis = [[1, 2], [3, 4], [5, 6]]
# arr = np.array(lis)
# print(arr[1, 0])  # 3
# print(arr[1][0])  # 3
# print(arr[:2, 1: 2])  # [[2] [4]]
# print(arr[:2][1: 2])  # [[3 4]]
# print(arr[...][1: 2])  # [[3 4]] 切片

# x = np.array([[1, 2], [3, 4], [5, 6]])
# 数组索引,等价于x[1] 和 x[2] 组成的数组; 数组索引不降维
# 第一步: x[1] → [3, 4]
# 第二步: x[2] → [5, 6]
# print(x[[1, 2]])  # [[3 4] [5 6]]

# 花式索引, 等价于x[0, 0] x[1, 1] 和 x[2, 0] 组成的数组
# 第一步: x[0, 0] → 1
# 第二步: x[1, 1] → 4
# 第三步: x[2, 0] → 5
# 第四步: x[0, 0], x[1, 1], x[2, 0]组成新数组
# print(x[[0, 1, 2], [0, 1, 0]])  # [1 4 5]

# 布尔索引
# print(x[[True, False, True]])  # [[1 2] [5 6]]
# print(x < 4)
# '''
# [[ True  True]
#  [ True False]
#  [False False]]
# '''
# print(x[x < 4])  # [1 2 3]
# print(x[np.array([[True, True], [True, False], [False, False]])])  # [1 2 3]


# np.resize(a, new_shape)  返回具有指定形状的新数组
# ndarray.resize(new_shape)  直接修改原数组的形状,无返回值
# a = np.array([[0, 1], [2, 3]])
# print(np.resize(a, (1, 2)))  # [[0 1]]
# print(np.resize(a, (2, 4)))
'''
[[0 1 2 3]
 [0 1 2 3]]
'''
# a.resize(1, 4)
# print(a)  # [[0 1 2 3]]
# a.resize((2, 4))
# print(a)
'''
[[0 1 2 3]
 [0 0 0 0]]
'''
# 当数组的总大小不变时, 应使用reshape
# 而resize是允许总大小发生变化的
# print(np.reshape(a, (1, 4)))  # 报错, 当改变原数组的大小时, reshape会报错


# ndarray.flatten()  返回扁平化到一维的数组
# a = np.array([[1, 2], [3, 4], [5, 6]])
# print(a.flatten())  # [1 2 3 4 5 6]


# ndarray.T  转置数组, 等价于a.T.shape == a.shape[::-1]
# a = np.array([[1, 2], [3, 4], [5, 6]])
# print(a)
'''
[[1 2]
 [3 4]
 [5 6]]
'''
# print(a.T)
'''
[[1 3 5]
 [2 4 6]]
'''

# a = np.array([1, 2, 3, 4, 5, 6])
# print(a)  # [1 2 3 4 5 6]
# print(a.T)  # [1 2 3 4 5 6]


# np.swapaxes(a, axis1, axis2)  交换数组的两个轴
# x = np.array([[1, 2, 3]])
# print(x)  # [[1 2 3]]
# print(x.shape)  # (1, 3)
# y = np.swapaxes(x, 0, 1)
# print(y.shape)  # (3, 1)
# print(y)
'''
[[1]
 [2]
 [3]]
'''

# x = np.arange(6).reshape((1, 2, 3))
# print(x)
'''
[[[0 1 2]
  [3 4 5]]]
'''
# print(x.shape)  # (1, 2, 3)
# y = np.swapaxes(x, 0, 2)
# print(y)
'''
[[[0]
  [3]]

 [[1]
  [4]]

 [[2]
  [5]]]
'''
# print(y.shape)  # (3, 2, 1)


# np.transpose(a, axes=None)  通过axes参数排列数组的shape, 如果axes省略,则transpose(a).shape==a.shape[::-1]
# a = np.ones((2, 3, 4, 5))
# print(np.transpose(a).shape)  # (5, 4, 3, 2)

# a = np.ones((1, 2, 3))
# print(np.transpose(a, (1, 0, 2)).shape)  # (2, 1, 3)

# a = np.array([1, 2, 3, 4])
# print(np.transpose(a))  # [1 2 3 4]


# np.expand_dims(a, axis)  扩展数组的形状
# x = np.array([1, 2])
# print(x.shape)  # (2,)

# y = np.expand_dims(x, axis=0)
# print(y.shape)  # (1, 2)

# y = np.expand_dims(x, axis=1)
# print(y.shape)  # (2, 1)

# y = np.expand_dims(x, axis=(0, 1))
# print(y.shape)  # (1, 1, 2)

# y = np.expand_dims(x, axis=(2, 0))
# print(y.shape)  # (1, 2, 1)


# np.squeeze(a, axis=None)  从给定数组的形状中删除一维的条目
# x = np.array([[[0], [1], [2]]])
# print(x.shape)  # (1, 3, 1)

# print(np.squeeze(x).shape)  # (3,)
# print(np.squeeze(x, axis=0).shape)  # (3, 1)
# print(np.squeeze(x, axis=2).shape)  # (1, 3)


# np.comcatenate((a1, a2,...), axis=0)  沿现有轴连接一系列数组, 如果axis为None, 则数组在使用前会被扁平化
# a = np.array([[1, 2], [3, 4]])
# b = np.array([[5, 6]])
# print(np.concatenate((a, b), axis=0))
'''
[[1 2]
 [3 4]
 [5 6]]
'''
# print(b.T)
'''
[[5]
 [6]]
'''
# print(np.concatenate((a, b.T), axis=1))
'''
[[1 2 5]
 [3 4 6]]
'''
# print(np.concatenate((a, b), axis=None))  # [1 2 3 4 5 6]


# np.stack(arrays, axis=0)  arrays: Sequence[ArrayLike] 沿新轴连接一系列数组
# arrays = [np.ones((3, 4)) for _ in range(5)]
# print(arrays)
# print(np.stack(arrays, axis=0).shape)  # (5, 3, 4)
# print(np.stack(arrays, axis=1).shape)  # (3, 5, 4)
# print(np.ones((3, 5, 4)))
# print(np.stack(arrays, axis=2).shape)  # (3, 4, 5)
# print(np.stack(arrays, axis=-1).shape)  # (3, 4, 5)


# np.hstack(tup)
# tup: Squence[ArrayLike]
# 通过水平堆叠来生成数组
# 根据1轴进行拼接, 如果是一维数据则根据0轴拼接
# a = np.array((1, 2, 3))
# b = np.array((4, 5, 6))
# print(np.hstack((a, b)))  # [1 2 3 4 5 6]
#
# a = np.array(([1], [2], [3]))
# b = np.array(([4], [5], [6]))
# print(np.hstack((a, b)))
'''
[[1 4]
 [2 5]
 [3 6]]
'''


# np.vstack(tup)
# tup: Sequence[ArrayLike]
# 通过垂直堆叠来生成数组
# 根据0轴进行拼接, 如果是一维(N,)数组, 则转成二维(1, N)数组, 再根据0轴拼接
# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])
# print(np.vstack((a, b)))
'''
[[1 2 3]
 [4 5 6]]
'''

# a = np.array([[1], [2], [3]])
# b = np.array([[4], [5], [6]])
# print(np.vstack((a, b)))
'''
[[1]
 [2]
 [3]
 [4]
 [5]
 [6]]
'''


# np.repeat(a, repeats, axis=None)
# repeats: 重复次数
# axis: 指定重复值的轴, 没指定时, 默认扁平化处理
# 重复数组中的元素
# print(np.repeat(3, 4))  # [3 3 3 3]

# x = np.array([[1, 2], [3, 4]])
# print(np.repeat(x, 2))  # [1 1 2 2 3 3 4 4]
# print(np.repeat(x, 3, axis=1))
'''
[[1 1 1 2 2 2]
 [3 3 3 4 4 4]]
'''
# print(np.repeat(x, [1, 2], axis=0))
'''
[[1 2]
 [3 4]
 [3 4]]
'''


# np.unique(ar, return, index=False, return_inverse=False, return_counts=True, axis=None)
# ar: 输入的数组
# return_index: 为True时, 还会返回新数组元素在旧数组中的下标
# return_inverse: 为True时, 还会返回旧数组元素在新数组中的下标
# return_counts: 为True时, 还会返回去重数组中的元素在原数组中的出现次数
# axis: 指定操作的轴, 没指定时, 默认扁平化处理
# 返回数组中排序的唯一元素, 重复元素会被去除, 只保留一个
# print(np.unique([3, 3, 1, 1, 2, 2]))  # [1 2 3]

# a = np.array([[1, 1], [2, 3]])
# print(np.unique(a))  # [1 2 3]

# a = np.array([[1, 0, 0], [1, 0, 0], [2, 3, 4]])
# print(np.unique(a, axis=0))
'''
[[1 0 0]
 [2 3 4]]
'''

# a = np.array([1, 2, 6, 4, 2, 3, 2])
# print(np.unique(a, return_index=True))  # (array([1, 2, 3, 4, 6]), array([0, 1, 5, 3, 2]))
# print(np.unique(a, return_inverse=True))  # (array([1, 2, 3, 4, 6]), array([0, 1, 4, 3, 1, 2, 1]))
# print(np.unique(a, return_counts=True))  # (array([1, 2, 3, 4, 6]), array([1, 3, 1, 1, 1]))


# np.dot(a, b)  两个数组的点积
# a = [1, 2, 3]
# b = [1, 0, 2]
# print(np.dot(a, b))  # 7

# a = [[1, 0], [0, 1]]
# b = [[4, 1], [2, 2]]
# print(np.dot(a, b))
'''
[[4 1]
 [2 2]]
'''

# print(np.dot(3, 4))  # 12

# a = 2
# b = [[4, 1], [2, 2]]
# print(np.dot(a, b))
'''
[[8 2]
 [4 4]]
'''

# a = [3, 5]
# b = [[4, 1], [2, 3]]
# print(np.dot(a, b))  # [22 18]

# a = [[4, 1], [2, 3]]
# b = [3, 5]
# print(np.dot(a, b))  # [17 21]


# np.matmul(x1, x2)  @操作符也可表示  两个数组的矩阵乘积
# a = np.array([[1, 0], [0, 1]])
# b = np.array([[4, 1], [2, 2]])
# print(np.matmul(a, b))
'''
[[4 1]
 [2 2]]
'''
# print(a @ b)
'''
[[4 1]
 [2 2]]
'''

# a = np.array([[1, 0], [0, 1]])
# b = np.array([1, 2])
# print(np.matmul(a, b))  # [1 2]
# print(a @ b)  # [1 2]


# np.greater(x1, x2)
# x1, x2的形状必须相同, 或者可以广播
# 按元素判断x1 > x2的结果
# print(np.greater([4, 2], [2, 2]))  # [ True False]

# a = np.array([[4, 2], [3, 1]])
# b = np.array([[2, 2]])
# print(np.greater(a, b))
'''
[[ True False]
 [ True False]]
'''
# print(a > b)
'''
[[ True False]
 [ True False]]
'''


# np.greater_equal(x1, x2)
# x1, x2的形状必须相同,或者可以广播
# 按元素判断x1 >= x2的结果
# print(np.greater_equal([4, 2], [2, 2]))  # [ True  True]

# a = np.array([[4, 2], [3, 1]])
# b = np.array([2, 2])
# print(np.greater_equal(a, b))
'''
[[ True  True]
 [ True False]]
'''
# print(a >= b)
'''
[[ True  True]
 [ True False]]
'''


# np.less(x1, x2)
# x1, x2的形状必须相同,或者可以广播
# 按元素判断x1 < x2的结果
# print(np.less([4, 2], [2, 2]))  # [False False]

# a = np.array([[4, 2], [3, 1]])
# b = np.array([[2, 2]])
# print(np.less(a, b))
'''
[[False False]
 [False  True]]
'''
# print(a < b)
'''
[[False False]
 [False  True]]
'''


# np.less_equal(x1, x2)
# x1, x2的形状必须相同,或者可以广播
# 按元素判断x1 <= x2的结果
# print(np.less_equal([4, 2], [2, 2]))  # [False  True]

# a = np.array([[4, 2], [3, 1]])
# b = np.array([[2, 2]])
# print(np.less_equal(a, b))
'''
[[False  True]
 [False  True]]
'''
# print(a <= b)
'''
[[False  True]
 [False  True]]
'''


# np.equal(x1, x2)
# x1, x2的形状必须相同,或者可以广播
# 按元素判断x1 == x2的结果
# print(np.equal([4, 2], [2, 2]))  # [False  True]

# a = np.array([[4, 2], [3, 1]])
# b = np.array([[2, 2]])
# print(np.equal(a, b))
'''
[[False  True]
 [False False]]
'''
# print(a == b)
'''
[[False  True]
 [False False]]
'''


# np.not_equal(x1, x2)
# x1, x2的形状必须相同,或者可以广播
# 按元素判断x1 != x2的结果
# print(np.not_equal([4, 2], [2, 2]))  # [ True False]

# a = np.array([[4, 2], [3, 1]])
# b = np.array([[2, 2]])
# print(np.not_equal(a, b))
'''
[[ True False]
 [ True  True]]
'''
# print(a != b)
'''
[[ True False]
 [ True  True]]
'''

