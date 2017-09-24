#在指定方形内，给出4个参数：n,p,min,max.画出n个圆形，其中为黑色的概率是p,圆的最小半径min, 最大半径为max

import sys
import random
import optparse
from stdpackage import stddraw

n = 100
p = 0.3
min = 0.05
max = 0.2

def main():


#     parser = optparse.OptionParser("""\
# usage: %prog [options] infile outfile
#
# draw circles in random location ,with random radius and color.""")
#
#     parser.add_option("-n", "--number", dest="n",
#             help=("input the number"))
#
#     parser.add_option("-p", "--possibility", dest="p",
#             help=("input the possibility in black"))
#
#
#     opts, args = parser.parse_args()
#
#     n = int(opts.n)
#     p = float(opts.p)


    stddraw.setXscale(0,2)
    stddraw.setYscale(0,2)


    i = 0
    while i < n:
        x = 2*random.random()
        y = 2*random.random()
        r = 0.02*random.randrange(1,5)
        color = stddraw.BLACK if random.random()<p else stddraw.BLUE
        stddraw.setPenColor(color)
        stddraw.filledCircle(x,y,r)

        i +=1
        stddraw.show(10)


main()