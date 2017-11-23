#渗透系统输入／输出

import sys
from stdpackage import stdarray,stddraw,stdio,stdrandom

def random(n,p):
    a = stdarray.create2D(n,n,False)
    for i in range(n):
        for j in range(n):
            a[i][j]=stdrandom.bernoulli(p)

    return a

def draw(a,which):

    n = len(a)
    stddraw.setXscale(-1,n)
    stddraw.setYscale(-1,n)
    if which == False:
        for i in range(n):
            for j in range(n):
                if a[i][j] == which:
                    stddraw.filledSquare(j,n-i-1,0.5)

    elif which == True:
        Li = []

        for i in range(n):
            for j in range(n):
                print(i,j)
                if a[i][j] == False:
                    Li.append(j)
                    print('{0} is false'.format(j))
                if a[i][j] == which and (j not in Li):
                    print('draw at({0},{1})'.format(i,j))

                    stddraw.filledSquare(j,n-i-1,0.5)



def main():
    n = int(sys.argv[1])
    p = float(sys.argv[2])
    test = random(n,p)
    stddraw.setPenColor(stddraw.BLACK)
    draw(test,False)
    stddraw.setPenColor(stddraw.BLUE)
    draw(test,True)
    stddraw.show()

if __name__ == '__main__':main()