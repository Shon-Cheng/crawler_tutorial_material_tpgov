# 載入 numpy 套件
import numpy as np
# 逐元運算(elementwise)
# data1 = np.array([3,2,10])
# data2 = np.array([1,3,6])

# 矩陣運算(matrix)
# data1 = np.array([
#     [1,3]
# ])
# data2 = np.array([
#     [2,-1,3],
#     [-2,4,1]
# ])
# result1 = data1.dot(data2)
# result2 = np.outer(data1,data2)
# print(result2)

# 統計運算(statistics)
data = np.array([
    [2,1,7],
    [-5,3,8]
])
# result = data.sum(axis = 0)
# print(result)
# result2 = data.sum(axis = 1)
# print(result2)
data2 = np.array([
    [
        [1,2,3],[4,5,6]
    ],
    [
        [7,8,9],[10,11,12]
    ]
])
result = data2.sum(axis = 0)
print(result)
result2 = data2.sum(axis = 1)
print(result2)
result3 = data2.sum(axis = 2)
print(result3)