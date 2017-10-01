#有重力效果的球

import math
from stdpackage import stddraw,stdarray,stdaudio

stddraw.setXscale(-1.0,1.0)
stddraw.setYscale(-1.0,1.0)

DT = 10
RADIUS = 0.1
r1x = 0.480
r1y = 0.860
v1x = 0.015
v1y = 0.0
g = -0.001
f = 0.005
position1 = [(r1x,r1y)]

SPS = 44100
CONCERT_A = 330.0
duration = 0.1
n = int(duration*SPS)
pitch = 1
hz = CONCERT_A*(2**(pitch/12.0))

samples = stdarray.create1D(n+1,0.0)
for i in range(n+1):
        samples[i] = math.sin(2.0*math.pi*i*hz/SPS)

changepoint = []

while True:

    if abs(r1x+v1x)+RADIUS>1.0:
        v1x = -v1x

        stdaudio.playSamples(samples)


    v1y +=g
    if abs(r1y + v1y)+RADIUS >1.0:
        v1y = -v1y
        stdaudio.playSamples(samples)

    r1x = r1x+v1x
    r1y = r1y + v1y
    if r1y >= 0.860:
        v1y = 0

    position1.append((r1x,r1y))

    stddraw.clear(stddraw.LIGHT_GRAY)

    stddraw.setPenColor(stddraw.BLACK)

    stddraw.filledCircle(r1x,r1y,RADIUS)

    stddraw.show(DT)