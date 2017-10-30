import sys
from stdpackage import stdarray,stddraw,stdio,stdrandom

n = int(sys.argv[1])
probabilities = stdarray.readFloat1D()
cx = stdarray.readFloat2D()
cy = stdarray.readFloat2D()

x = 0.0
y = 0.0

stddraw.setPenRadius(0.0)
for i in range(n):
    r = stdrandom.discrete(probabilities)
    x0 = cx[r][0]*x + cx[r][1]*y+cx[r][2]
    y0 = cy[r][0]*x + cy[r][1]*y+cy[r][2]
    x = x0
    y = y0
    stddraw.point(x,y)


stddraw.show()