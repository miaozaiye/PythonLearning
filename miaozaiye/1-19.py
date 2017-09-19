#draw chessboard filled with black and red, with given number n.
#start with red at the left bottom.

import sys
from stdpackage import stddraw


def draw_chessboard(n,r,x_group,y_group):
    for x_i in range(n):
        for y_i in range(n):
            print(x_i,y_i)
            stddraw.setPenColor(stddraw.RED if (x_i+y_i)%2==0 else stddraw.BLACK)
            stddraw.filledSquare(x_group[x_i],y_group[y_i],r)
            stddraw.setPenColor(stddraw.WHITE)
            stddraw.text(x_i,y_i,'{0},{1}'.format(x_i,y_i))

    stddraw.show()


def draw_ball():



def main():
    n = int(sys.argv[1]) # get input value of n

    scale= (-1,1)
    l = scale[1]-scale[0]
    r = l/(n*2) # calculate r
    x_group = [(2*i+1)*r-1 for i in range(n)]  #set X location of each column
    y_group = [(2*i+1)*r-1 for i in range(n)]  #set Y locaion of each column

    stddraw.setXscale(scale[0],scale[1]) #set scale of canvas
    stddraw.setYscale(scale[0],scale[1])

    draw_chessboard(n,r,x_group,y_group)




main()