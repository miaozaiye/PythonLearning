#根据命令行输入的整数N，画出一个圆周上等间隔的N个点；根据输入的浮点数P（取值范围为0-1），按概率P在任意两点之间绘制
#连接线。
import math
import random
from stdpackage import stddraw

class Points():
    def __init__(self,n):
        self.x = []
        self.y = []
        for i in range(1,n+1):
            self.x.append(1 * math.cos(2*i*math.pi/n))
            self.y.append(1 * math.sin(2*i*math.pi/n))




class Circle(Points):
    def __init__(self,n = 0,p = 0.0):
        super().__init__(n)
        self.p = p
        print(self.p,self.x,self.y)

    def possibility(self):
        a = random.random()
        return True if a < self.p else False

    def line(self):
        stddraw.setYscale(-1.5,1.5)
        stddraw.setXscale(-1.5,1.5)
        try:
            done_point = []
            for (x1,y1) in zip(self.x,self.y):
                if (x1,y1) not in done_point:
                    done_point.append((x1,y1))

                    for (x2,y2) in zip(self.x,self.y):
                        if (x1,y1) != (x2,y2) and self.possibility():
                            stddraw.setPenColor(stddraw.LIGHT_GRAY)
                            stddraw.setPenRadius(r = 0.01)
                            stddraw.line(x1,y1,x2,y2)
                        else:
                            pass
                else:
                    pass
            for (x,y) in zip(self.x,self.y):
                stddraw.setPenRadius(r = 0.02)
                stddraw.setPenColor(stddraw.BLACK)
                stddraw.point(x,y)
        except Exception:
            print(Exception)

    def show(self):
        stddraw.show()


a = Circle(n = 17,p = 0.25)
a.line()
a.show()