#matrix

'''
rand(m,n)  创建一个m*n 的矩阵，其各元素为0到1之间的随机浮点数
identy(n)  创建一个n*n 的单位矩阵
dot(v1,v2) 两个向量 v1 和 v2的点积
transpose(m) 矩阵的转置
add(m1,m2) 矩阵 m1 和 m2 的和
subtrac(m1,m2) 两者之差


'''

import random

def rand(m,n):
    matrix = [[random.random() for i in range(n)] for j in range(m)]
    return matrix

def identy(n):
    matrix = [[1 for i in range(n)] for j in range(n)]
    return matrix

def dot(v1,v2):
    assert len(v1[0]) == len(v2),'index does not match'
    matrix = rand(len(v1),len(v2[0]))
    for i in range(len(v1)):
        for j in range(len(v2[0])):
            matrix[i][j] = 0
            for m in range(len(v1[0])):
                matrix[i][j]+=v1[i][m]*v2[m][j]

    return matrix

def transpose(m):
    M = len(m)
    N = len(m[0])
    matrix = rand(N,M)
    for i in range(M):
        for j in range(N):
            matrix[i][j] = m[j][i]
    return matrix

v1 = [[1,2,3],
      [3,4,5]]
v2 = [[5,6,7,8],
      [3,6,8,2],
      [0,0,8,3]]

print(dot(v1,v2))
