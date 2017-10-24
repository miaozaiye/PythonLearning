import math
from stdpackage import stdarray,stdaudio,stdio

def superpose(a,b,aWeight,bWeight):
    c = stdarray.create1D(len(a),0.0)
    for i in range(len(a)):
        c[i] = aWeight*a[i]+bWeight*b[i]

    return c

def tone(hz,duration,sps=44100):
    n = int(sps*duration)
    a = stdarray.create1D(n+1,0.0)
    for i in range(n+1):
        a[i] = math.sin(2.0*math.pi*i*hz/sps)
    return a

def note(pitch,duration):
    hz= 440.0*(2.0**(pitch/12.0))
    lo = tone(hz/1.5,duration)
    hi = tone(hz*1.5,duration)
    harmonics = superpose(lo,hi,0.5,0.5)
    a = tone(hz,duration)
    return superpose(harmonics,a,0.6,0.4)

while not stdio.isEmpty():
    pitch = stdio.readInt()
    duration = stdio.readFloat()
    a = note(pitch,duration)
    stdaudio.playSamples(a)

stdaudio.wait()