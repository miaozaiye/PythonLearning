#布朗桥，模拟两点之间随机游走模型下的连线，类似于股票走势图
'''

1。 X_0， X_1 是起点和终点，通过n控制步长
2。 x_m = (X[i]+x[i+1])/2
3。 y = (Y[i]+Y[i+1])/2+thou ( 随机偏移变量）
4。 当X集合长度 == n+2 时，return
'''
import random
from stdpackage import stddraw

def benouli():
    a = -1 if random.random()<0.5 else 1
    return a

def brownian(x0,y0,x1,y1,n):

    if n < 1:
        print(B_list)
        print ('now return')
        return

    print(B_list)
    thou = benouli()*random.random()
    x_m = x0+(x1-x0)/2
    y_m = y0+(y1-y0)/2+thou
    ind = B_list.index([x0,y0])
    print(ind)
    B_list.insert(ind+1,[x_m,y_m])

    brownian(x0,y0,x_m,y_m,n/2)
    brownian(x_m,y_m,x1,y1,n/2)

def draw(list):
    for i in range(len(list)-1):
        x0 = list[i][0]
        y0 = list[i][1]
        x1 = list[i+1][0]
        y1 = list[i+1][1]
        stddraw.line(x0,y0,x1,y1)
        stddraw.show(20)

def main(x_0,x_1,y_0,y_1,n):
    stddraw.setXscale(0,6)
    stddraw.setYscale(0,10)
    global B_list
    B_list= [[x_0,y_0],[x_1,y_1]]
    print(B_list)

    brownian(x_0,y_0,x_1,y_1,n)
    print(B_list)
    draw(B_list)

main(1,5,2,8,50)