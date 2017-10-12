#在指定方形内，给出4个参数：n,p,min,max.画出n个圆形，其中为黑色的概率是p,圆的最小半径min, 最大半径为max

import sys
import random
import optparse
from stdpackage import stddraw
from stdpackage import stdarray
from stdpackage import stdaudio
import math

SPS = 44100
CONCERT_A = 440.0

pitch0 = 6





n = 200
p = 0.3
min = 0.05
max = 0.2

def play_tune(x,y,r):
    pitch = (pitch0) * math.sqrt(x*x+y*y)/10
    duration = float(r)*3
    n1 = int(SPS*duration)
    hz = CONCERT_A*(2**(pitch/12.0))
    samples = stdarray.create1D(n1+1,0.0)
    for i in range(n+1):
        samples[i] = math.sin(2.0*math.pi*i*hz/SPS)
    stdaudio.playSamples(samples)


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
        r = 0.01*random.randrange(1,30)
        color = stddraw.BLUE if random.random()<p else stddraw.BOOK_RED
        stddraw.setPenColor(color)
        stddraw.filledCircle(x,y,r)

        i +=1

        play_tune(x,y,r)
        stddraw.show(10)


main()