# 垂直渗透系统检测

from stdpackage import stdarray,stdio

def flow(isOpen):
    n = len(isOpen)
    isFull = stdarray.create2D(n,n,False)

    #以下为脚手架基础上，新增的部分
    for j in range(n):
        isFull[0][j]=isOpen[0][j]
    for i in range(1,n):
        for j in range(n):
            if isOpen[i-1][j] and isOpen[i][j]:
                isFull[i][j] = True


    return isFull

def percolates(isOpen):
    isFull = flow(isOpen)
    n = len(isFull)
    for j in range(n):
        if isFull[n-1][j]:return True
    return False

def main():
    isOpen = stdarray.readBool2D()
    stdarray.write2D(flow(isOpen))
    stdio.writeln(percolates(isOpen))

if __name__ == '__main__':
    main()
