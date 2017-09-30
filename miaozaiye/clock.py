#绘制一个时钟，有秒钟，分钟，时钟指针
#秒钟指针每1秒移动一次。
#用户可以设置小时，分钟。

'''
1. r = 1 大圆，分12等分
2。时钟指针 Hour_L 0.3, 分钟指针 Min_L 0.45, 秒钟指针 Sec_L 0.6
3. 每过1秒钟，秒钟指针移动1/60 圈；每过 1分钟， 分钟指针移动 1／60圈，每过1小时，时钟指针移动1／12 圈
'''

from stdpackage import stddraw
from stdpackage import stdarray
import math
import sys


def draw_clock(H = 0,M = 0, S = 0):
    stddraw.setXscale(-1.5,1.5)
    stddraw.setYscale(-1.5,1.5)

    R = 1.1
    Hour_L = 0.4
    Min_L = 0.55
    Sec_L = 0.7
    Hour_count = 0

    Hour_X = stdarray.create1D(12,0)
    Hour_Y = stdarray.create1D(12,0)


    for i in range(1,13):
        Hour_X[i-1]=1*math.cos(-(i/12*2*math.pi-1/2*math.pi))
        Hour_Y[i-1]=1*math.sin(-(i/12*2*math.pi-1/2*math.pi))

    stddraw.setFontSize(20)

    if H>11:
            print('H is {0}'.format(H))
            H = H%12
            Hour_count = 1

    while True:
        for H_i in range(H,12):

            angle_H = H_i*2*math.pi/12-1/2*math.pi
            if H_i == 11:
                H_i = 0
                Hour_count +=1

            if Hour_count % 2 == 0:
                text = 'morining'
            else:
                text = 'afternoon'

            for M_i in range(M,60):

                angle_M = M_i*2*math.pi/60-1/2*math.pi

                for S_i in range(S,60):
                    stddraw.clear()
                    stddraw.circle(0,0,R)
                    for i in range(1,13):
                        stddraw.text(Hour_X[i-1],Hour_Y[i-1],str(i))
                    stddraw.text(0,0.85,text)

                    stddraw.setPenRadius(0.02)
                    stddraw.line(0,0,Hour_L*math.cos(-angle_H),Hour_L*math.sin(-angle_H))
                    stddraw.setPenRadius(0.01)
                    stddraw.line(0,0,Min_L*math.cos(-angle_M),Min_L*math.sin(-angle_M))
                    stddraw.setPenRadius(0.005)
                    angle_s = S_i*2*math.pi/60-1/2*math.pi
                    stddraw.line(0,0,Sec_L*math.cos(-angle_s),Sec_L*math.sin(-angle_s))
                    stddraw.show(1000)

def main():


    angle_H = int(sys.argv[1])
    angle_M = int(sys.argv[2])
    angle_s = int(sys.argv[3])

    draw_clock(angle_H,angle_M,angle_s)

main()




