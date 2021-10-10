a = [
    [0,2],
    [1,2],
    [2,2],
    [3,2],
    [4,2],
    [5,2],
    [6,2],
    [7,2],
    [8,2],
    [9,2]
]
import numpy as np
a = np.array(a)
print(a[:,0])
print(a[:,1])


# https://wangyeming.github.io/2018/11/12/numpy-meshgrid/
x = [1,2,3,4]
y = [5,6,7]
xx,yy = np.meshgrid(x,y)
print(xx)
print(yy)