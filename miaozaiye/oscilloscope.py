#示波器，程序模拟示波器的输入，产生李萨如模式
'''

当两个相互垂直的周期扰动同时发生时，结果产生该模式图案

x(t) = A_x*sin(w_x*t+theta_x)
y(t) = A_y*sin(w_x*t+theta_y)

程序带六个命令行参数： A_x,A_y,w_x,w_y,theta_x,theta_y
'''

import math
import sys
from stdpackage import stddraw,stdaudio

def draw(x1,x0,y1,y0):
    stddraw.line(x0,y0,x1,y1)
    pass

def main():
    A_x,A_y,w_x,w_y,theta_x,theta_y = sys.argv[1:]
    A_x = float(A_x)
    A_y = float(A_y)
    w_x = float(w_x)
    w_y = float(w_y)
    theta_x = float(theta_x)
    theta_y = float(theta_y)
    i = 0
    X = []
    Y = []
    stddraw.setXscale(-4,4)
    stddraw.setYscale(-4,4)
    while True:
        x = A_x*math.sin(w_x*i+theta_x)
        y = A_y*math.sin(w_y*i+theta_y)
        X.append(x)
        Y.append(y)
        if i <1:
            pass
        else:
            draw(X[i],X[i-1],Y[i],Y[i-1])
            stddraw.show(20)
        i +=1


main()