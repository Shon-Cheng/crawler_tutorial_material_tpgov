import numpy as np
data1 = np.array([
    [2,1]
])
data2 = np.array([
    [3,2,0],
    [3,1,-1]
])
y = data2.cumsum()
x = np.outer(data1,data2)
print(y)