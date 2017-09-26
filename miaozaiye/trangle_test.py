import math


import sys
sys.path.append('/Users/Jane/Desktop/PythonLearning/miaozaiye/stdpackage')

from stdpackage import stddraw

# t = math.sqrt(3.0/2.0)
# stddraw.line(0.0,0.0,0.0,1.0)
# stddraw.line(1.0,0.0,0.5,t)
# stddraw.line(0.5,t,0.0,0.0)
# stddraw.point(0.5,t/3.0)
# stddraw.show()

# stddraw.square(.2,.8,.1)
# stddraw.filledSquare(.8,.8,.2)
# stddraw.circle(.8,.2,.2)
# xd=[.1,.2,.3,.2]
# yd=[.2,.3,.2,.1]
# stddraw.filledPolygon(xd,yd)
# stddraw.text(.2,.5,'black text')
# stddraw.setPenColor(stddraw.WHITE)
# stddraw.text(.8,.8,'white text')
# stddraw.show()

from miaozaiye.stdpackage1 import stdarray


n = 2000

x = stdarray.create1D(n+1,0.0)
y = stdarray.create1D(n+1,0.0)

for i in range(n+1):
    x[i] = math.pi*i/n
    y[i] = math.sin(4.0*x[i]) + math.sin(20.0 * x[i])

stddraw.setXscale(0,math.pi)
stddraw.setYscale(-2.0,+2.0)
for i in range(n):
    stddraw.line(x[i],y[i],x[i+1],y[i+1])

stddraw.show()
