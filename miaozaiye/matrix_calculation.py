#创建一个矩阵类，可以根据要求创建不同维度的矩阵，然后再进行矩阵的加减乘除运算


def creat2D(row,line,value = 0):
    assert isinstance(row,int),'row number must be int'
    assert isinstance(line,int),'line number must be int'
    print()
    array= []
    array_line=[]

    array = [None] * row
    for index in range(row):
        array[index] = [value]*line
    # for i in range(row+1):
    #     if len(array) !=0:
    #         array.append(array_line)
    #         array_line = []
    #     else:
    #         pass
    #     for j in range(line):
    #         array_line.append(value)
    #     print(array_line)
    return array

A = creat2D(2,2,0)


def array_plus(a1,a2):
    row = len(a1)
    line = len(a1[0])
    c = creat2D(row,line,0)
    for i in range(row):
        for j in range(line):
            c[i][j] = a1[i][j]+a2[i][j]
    return c


def array_dotmtp(a1,a2):
    assert len(a1[0])==len(a2), "a1's line must equal to a2's row"
    row = len(a1)
    line = len(a1[0])
    c = creat2D(row,line)
    for i in range(row):
        for j in range(line):
            for k in range(row):
                c[i][j] += a1[i][k]*a2[k][j]

    return c


A[0][1] = 1
B = creat2D(2,2,1)
C = creat2D(2,3,2)

print(A,B)
print(array_plus(A,B))
print(array_dotmtp(A,B))
array_dotmtp(B,C)