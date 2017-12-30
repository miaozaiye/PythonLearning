from stdpackage import stddraw,stdio,stdarray,instream
from stdpackage.instream import InStream
import math
import sys


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

    def direction(self): return self.scale(1.0/abs(self))
    def __getitem__(self,i): return self._coords[i]
    def __abs__(self): return math.sqrt(self.dot(self))
    def __len__(self): return self._n
    def __str__(self): return str(self._coords)


class Body:
    def __init__(self,r,v,mass):
        self._r = r
        self._v = v
        self._mass = mass

    def move(self,f,dt,list):
        # print('move')
        a = f.scale(1.0/self._mass)
        self._v = self._v+a.scale(dt)

        if ( self._r + self._v.scale(dt)) in list:
            self._v = -self._v
        self._r = self._r+self._v.scale(dt)
        # print(self._r,self._v)

    def get_r(self):
        return self._r
    def forceFrom(self,other):
        G = 6.67e-11
        delta = other._r - self._r

        dist = abs(delta)
        m1 = self._mass
        m2 = other._mass
        magnitude = G*m1*m2/(dist*dist)
        return delta.direction().scale(magnitude)

    def draw(self):
        if self._mass == 5.97e25:
            stddraw.setPenRadius(0.0125)
        else:
            stddraw.setPenRadius(0.025)
        stddraw.point(self._r[0],self._r[1])



class Universe:
    def __init__(self,filename):
        instream = InStream(filename)
        n = instream.readInt()
        radius = instream.readFloat()
        stddraw.setXscale(-radius,+radius)
        stddraw.setYscale(-radius,+radius)

        self._bodies = stdarray.create1D(n)
        for i in range(n):
            rx = instream.readFloat()
            ry = instream.readFloat()
            vx = instream.readFloat()
            vy = instream.readFloat()
            mass = instream.readFloat()
            r = Vector([rx,ry])
            v = Vector([vx,vy])
            self._bodies[i] = Body(r,v,mass)

    def increaseTime(self,dt):
        # print('increasetime')
        n = len(self._bodies)
        f = stdarray.create1D(n,Vector([0,0]))
        for i in range(n):
            for j in range(n):
                if i != j :
                    bodyi = self._bodies[i]
                    bodyj = self._bodies[j]
                    f[i] =f[i] + bodyi.forceFrom(bodyj)
        r_list = []
        for i in range(n):
            # print('r_list is:',r_list)
            self._bodies[i].move(f[i],dt,r_list)
            r_list.append(self._bodies[i].get_r())

    def draw(self):
        for body in self._bodies:
            # print('draw body at,',body.get_r())
            body.draw()


def main():
    universe = Universe(sys.argv[1])
    dt = float(sys.argv[2])
    count = 0
    while True:
        universe.increaseTime(dt)
        stddraw.clear()
        universe.draw()
        stddraw.show(10)
        print(count)
        count +=1


if __name__ == '__main__':main()
