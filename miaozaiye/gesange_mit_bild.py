#用正弦波图形动态展示音符
'''

从标准输入读入音符（整数），持续时间（浮点数）
    画出该整数音符对应的波形，并持续对应时间
        基准单位波距：0.1 （440.0）

    播放该整数音符对应的声音，并持续对应时间

'''
import math
import sys
from stdpackage import stdarray
from stdpackage import stddraw
from stdpackage import stdio
from stdpackage import stdaudio

#initiate notes
A = 440.0
A_p = 466.16
B = 493.88
C =523.25
C_p = 554.37
D =587.33
D_p = 622.25
E = 659.26
F =698.46
F_p = 739.99
G = 783.99
G_p = 830.61

SPS = 44100
notes = [A,A_p,B,C,C_p,D,D_p,E,F,F_p,G,G_p]
print(notes[1])

class Note():
    def __init__(self,n,f):
        self.n = n
        self.f = f

    def audio_note(self):
        stddraw.setXscale(0,50)
        stddraw.setYscale(-10,10)

        print('enter audio_note')
        duration = self.f
        hz = notes[self.n-1]
        n = int(SPS*duration)
        samples = stdarray.create1D(n+1,0.0)
        for i in range(n+1):
            samples[i] = math.sin(2.0*math.pi*i*hz/SPS)
        print(samples)
        for i in range(0,n-100,100):
            stddraw.line(i/500,samples[i],(i+100)/500,samples[i+100])
        stddraw.show()
        stdaudio.playSample(samples)
        print('play')
        stdaudio.wait()




song1 = Note(2,0.5)

song1.audio_note()


