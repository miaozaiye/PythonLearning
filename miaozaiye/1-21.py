#输出花瓣图像
#not finished

import math
from stdpackage import stddraw

class Flower():
    def __init__(self,r,n):
        self.r = r
        self.n = 2*n if n%2==0 else n
        self.theta = 2*math.pi/(2*n) if n%2==0 else 2*math.pi/n

    def blome(self):
        stddraw.setXscale(-1.2,1.2)
        stddraw.setYscale(-1.2,1.2)
        x_list=[]
        y_list=[]
        for i in range(1,self.n+1):
            theta = self.theta
            for n in range(100):

                x =math.sin(theta)*math.cos(theta)
                y = math.sin(theta)*math.sin(theta)
                x_list.append(x)
                y_list.append(y)
                if n >0:
                    stddraw.line(x_list[n-1],y_list[n-1],x_list[n],y_list[n])
                    stddraw.show(50)

                theta += n*self.theta/100

a = Flower(1,5)
a.blome()