from stdpackage import stdaudio
from stdpackage import stdarray
import math
import sys

SPS = 44100
hz = 440.0
duration = 10.0
n = int(SPS*duration)
a = stdarray.create1D(n+1)
for i in range(n+1):
    a[i]=math.sin(2.0*math.pi*i*hz/SPS)

stdaudio.playSample(a)
stdaudio.wait()