import math
from stdpackage import stdarray
from stdpackage import stdaudio
from stdpackage import stdio
from stdpackage import stddraw

SPS = 44100
CONCERT_A = 440.0

stddraw.setXscale(0,50)
stddraw.setYscale(-20,20)
height = 1
while not stdio.isEmpty():

    pitch = stdio.readInt()
    duration = stdio.readFloat()
    hz = CONCERT_A*(2**(pitch/12.0))
    n = int(SPS*duration)
    samples = stdarray.create1D(n+1,0.0)
    for i in range(n+1):
        samples[i] = math.sin(2.0*math.pi*i*hz/SPS)
    stdaudio.playSamples(samples)


    for i in range(0,n-100,100):
        stddraw.line(i/500,samples[i]+20-height,(i+100)/500,samples[i+100]+20-height)
    stddraw.show(duration*1000)
    height +=2

stdaudio.wait()