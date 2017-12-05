from stdpackage import color,stddraw
import sys
from stdpackage.color import Color


r1 = int(sys.argv[1])
g1 = int(sys.argv[2])
b1 = int(sys.argv[3])
c1 = Color(r1,g1,b1)

r2 = int(sys.argv[4])
g2 = int(sys.argv[5])
b2 = int(sys.argv[6])
c2 = Color(r2,g2,b2)

stddraw.setPenColor(c1)
stddraw.filledSquare(.25,.5,.2)
stddraw.setPenColor(c2)
stddraw.filledSquare(.25,.5,.1)
stddraw.setPenColor(c2)
stddraw.filledSquare(.75,.5,.2)
stddraw.setPenColor(c1)
stddraw.filledSquare(.75,.5,.1)

stddraw.show()
