# -*- coding = utf-8 -*-
# @Time: 2024/5/21 16:47
# @Author: ZhouYanHui


# squares = []
#
# for x in range(10):
#     squares.append(x ** 2)
#
# print(squares)

# squares = [x ** 2 for x in range(10)]
#
# print(squares)

# result = []
# for x in [1, 2, 3]:
#     for y in [3, 1, 4]:
#         if x != y:
#             result.append((x, y))
#
# print(result)

# result = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
# print(result)

# matrix = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]]

# print([row[0] for row in matrix])

# result = [[row[i] for row in matrix] for i in range(3)]
# print(result)

# dic = {x: x**2 for x in range(4)}
# print(dic)

# dic = {x: x ** 2 for x in range(4) if x % 2 == 0}
# print(dic)
#
# print(zip((1, 2, 3), (4, 5, 6)))

# lis = [1, 2, 3]
#
# for item in lis:
#     print(item)
#     lis.remove(item)
#
# print(lis)
