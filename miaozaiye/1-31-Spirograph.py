#万花筒程序
'''
x(t) = (R+r)cos(t)-(r+a)cos((R+r)t/r)
y(t) = (R+e)sin(t)-(r+a)sin((R+r)t/r)

'''

import sys
import math
from stdpackage import stddraw,stdarray,stdaudio

SPS = 44100
CONCERT_A = 220.0

pitch0 = 3
duration = 0.5

n = int(SPS*duration)


def play_tune(x,y):
    pitch = (pitch0) * (x+y)/2
    hz = CONCERT_A*(2**(pitch/12.0))
    samples = stdarray.create1D(n+1,0.0)
    for i in range(n+1):
        samples[i] = math.sin(2.0*math.pi*i*hz/SPS)
    stdaudio.playSamples(samples)

def draw_spirograph(R,r,a):
    stddraw.setXscale(-40,40)
    stddraw.setYscale(-40,40)
    l = 1500
    x = stdarray.create1D(l,0)
    y = stdarray.create1D(l,0)
    for t in range(l):
        x[t] = (R+r)*math.cos(t) - (r+a) * math.cos((R+r)*t/r)
        y[t] = (R+r)*math.sin(t) - (r+a) * math.sin((R+r)*t/r)

    for t in range(l+1):
        if t >= l-1:
            pass
        else:
            if t ==0:
                stddraw.setPenColor(stddraw.RED)
            if t==l/3:
                stddraw.setPenColor(stddraw.DARK_BLUE)
            if t == 2*l/3:
                stddraw.setPenColor(stddraw.BOOK_BLUE)


            stddraw.line(x[t],y[t],x[t+1],y[t+1])
            play_tune(x[t],y[t])
            stddraw.show(5)
    stddraw.show()

def main():

    R = int(sys.argv[1])
    r = int(sys.argv[2])
    a = int(sys.argv[3])

    draw_spirograph(R,r,a)

main()