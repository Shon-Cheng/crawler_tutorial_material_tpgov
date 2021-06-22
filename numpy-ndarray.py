# 載入 numpy 套件
import numpy as np

# 建立一維陣列
# data = np.array([3, 2, 6, 4])
# print(data)
# data = np.empty(4) # 創造有四個資料的一維陣列, 資料未指定
# print(data)
# data = np.zeros(3) # 預設為用浮點數 也就是小數
# print(data)
# data = np.ones(4)
# print(data)
# data = np.arange(5)
# print(data)

# 建立二維陣列
# data = np.array([
#     [2,3,2],
#     [1,2,3],
#     [4,5,6]
# ])
# print(data)
# data = np.empty([3,3]) # 因為未指定 所以裡頭的數字會是隨機的
# print(data)
# data = np.ones([2,3])
# print(data)

# 建立三維陣列
# data = np.array([
#     [
#         [3,1],[1,2]
#     ],[
#         [2,5],[10,2]
#     ]
# ])
# print(data)
# data = np.zeros([3,1,3])
# print(data)

# 建立高維陣列
data = np.array([
    [
        [
            [1,2],[3,4]
        ],
        [
            [5,6],[7,8]
        ]

    ],
    [
        [
            [9,10],[11,12]
        ],
        [
            [13,14],[15,16]
        ]
    ]
])
print(data)
data = np.ones([2,1,1,2])
print(data)