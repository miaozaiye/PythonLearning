#scaffolding  脚手架程序

from stdpackage import stdarray,stdio

def flow(isOpen):
    n = len(isOpen)
    isFull = stdarray.create2D(n,n,False)
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
