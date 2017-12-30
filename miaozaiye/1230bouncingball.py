#用类定义刚性小球，以及球桌
'''

刚性小球特性：
1。 半径，质量，速度，位置。其中速度，位置为向量（Vector），半径，质量为标量
2。 r = r_0 + v*dt
3.  v = a*dt, 其中 a为垂直方向的
球桌特性：
1。 根据输入生成n个球
2。 小球碰到球桌边缘，则会反弹
3。 不同小球相撞，会交换动量（m1v1 = m2v2)
4。 每10毫秒绘制一次每个小球的位置

'''

from stdpackage import stddraw,stdarray
import sys
import math
import random

class Vector:
    def __init__(self,a):
        self._coords = a[:]
        self._n = len(a)

    def __add__(self,other):
        result = stdarray.create1D(self._n,0)
        for i in range(self._n):
            result[i] = self._coords[i]+other._coords[i]

        return Vector(result)


    def __sub__(self,other):
        result = stdarray.create1D(self._n,0)
        for i in range(self._n):
            result[i] = self._coords[i]-other._coords[i]

        return Vector(result)



    def dot(self,other):
        result = 0
        for i in range(self._n):
            result +=self._coords[i]*other._coords[i]
        return result

    def scale(self,alpha):
        result = stdarray.create1D(self._n,0)
        for i in range(self._n):
            result[i] = alpha * self._coords[i]

        return Vector(result)
    def getatt(self):
        return [self._coords]

    def direction(self): return self.scale(1.0/abs(self))
    def __getitem__(self,i): return self._coords[i]
    def __abs__(self): return math.sqrt(self.dot(self))
    def __len__(self): return self._n
    def __str__(self): return str(self._coords)


class Ball:
    def __init__(self,mass,radius,velocity,location):
        self.mass = mass
        self.radius = radius
        self.velocity = velocity
        self.location = location

    def move(self,f,dt):
        print('before move,',self.location)
        self.location = self.location+self.velocity.scale(dt)
        a = f.scale(1/self.mass)
        self.velocity = self.velocity + a.scale(dt)
        print('after move,',self.location)

    def draw(self):
        print('ball.draw')
        stddraw.setPenColor(stddraw.color.BLACK)
        print('this is location,',self.location.getatt())
        stddraw.filledCircle(self.location.getatt()[0][0],self.location.getatt()[0][1],self.radius)

class Table:
    def __init__(self,n):

        self._balls = stdarray.create1D(n)
        self._min = -50
        self._max = 50
        stddraw.setYscale(self._min,self._max)
        stddraw.setXscale(self._min,self._max)
        for i in range(n):
            mass = random.randint(1,10)
            radius = random.uniform(1,2)
            velocity = Vector([random.uniform(0,3),random.uniform(0,3)])
            location = Vector([random.uniform(0,10),random.uniform(5,10)])
            print('generate location:',location)
            ball = Ball(mass,radius,velocity,location)
            self._balls[i] = ball


    def hitball(self,i,j):
        print(self._balls[i].location.getatt(),self._balls[i].radius)
        if self._balls[i].location.getatt()[0][0]+self._balls[i].radius >= self._balls[j].location.getatt()[0][0]-self._balls[j].radius:
            if self._balls[i].location.getatt()[0][0]-self._balls[i].radius <= self._balls[j].location.getatt()[0][0]+self._balls[j].radius:
                if self._balls[i].location.getatt()[0][1]+self._balls[i].radius>=self._balls[j].location.getatt()[0][1]-self._balls[j].radius:
                    if self._balls[i].location.getatt()[0][1]-self._balls[i].radius<=self._balls[j].location.getatt()[0][1]+self._balls[j].radius:
                        return True

        return False



    def time_evolve(self,dt):
        print('time_evolve')
        for i in range(len(self._balls)):
            for j in range(len(self._balls)):
                if i !=j:
                    if self.hitball(i,j):
                        print('ball {0} heats ball {1} '.format(i,j))
                        tmp = self._balls[i].velocity
                        self._balls[i].velocity= self._balls[j].velocity.scale(self._balls[j].mass).scale(1/self._balls[i].mass)
                        self._balls[j].velocity = tmp.scale(self._balls[i].mass).scale(1/self._balls[j].mass)



            if self._balls[i].location.getatt()[0][0]-self._balls[i].radius < self._min or self._balls[i].location.getatt()[0][0]+self._balls[i].radius >self._max:
                self._balls[i].velocity = Vector([-self._balls[i].velocity.getatt()[0][0], self._balls[i].velocity.getatt()[0][1]])
            if self._balls[i].location.getatt()[0][1] -self._balls[i].radius<self._min or self._balls[i].location.getatt()[0][1]+self._balls[i].radius > self._max:
                self._balls[i].velocity = Vector([self._balls[i].velocity.getatt()[0][0], -self._balls[i].velocity.getatt()[0][1]])
            f = Vector([0,-0.9])
            self._balls[i].move(f,dt)

    def draw(self):
        for ball in self._balls:
            ball.draw()


def main():
    n = int(sys.argv[1])
    time = float(sys.argv[2])

    table = Table(n)
    while True:
        table.time_evolve(time)
        table.draw()
        stddraw.show(20)
        stddraw.clear()


if __name__ == '__main__': main()

