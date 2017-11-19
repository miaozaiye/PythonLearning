#generate recursive tree
'''

1. get input of number of generations, length ratio a%, b%,c%;angle A,B,C
2. recursive part:
a. original main line x,y
b. branch 1 x1,y1 = x+r * a%*cos A, y+r*a%sinA
'''
import math
from unittest.mock import _ANY

from stdpackage import stddraw

n = 7
a = 0.7
b = 0.5
c = 0.65
A = 30
B = 5
C = -25
r = 5

stddraw.setXscale(-10,20)
stddraw.setYscale(0,30)

def recursive_tree(n,A0,r,x0,y0):
    if n == 0:

        return
    xa = x0+r*math.cos((A0+A)/360*2*math.pi)
    ya = y0+r*math.sin((A0+A)/360*2*math.pi)
    stddraw.line(x0,y0,xa,ya)
    stddraw.show(50)
    recursive_tree(n-1,A0+A,r*a,xa,ya)

    xb = x0+r*math.cos((A0+B)/360*2*math.pi)
    yb = y0+r*math.sin((A0+B)/360*2*math.pi)
    stddraw.line(x0,y0,xb,yb)
    stddraw.show(50)
    recursive_tree(n-1,A0+B,r*b,xb,yb)

    xc = x0+r*math.cos((A0+C)/360*2*math.pi)
    yc = y0+r*math.sin((A0+C)/360*2*math.pi)
    stddraw.line(x0,y0,xc,yc)
    stddraw.show(50)
    recursive_tree(n-1,A0+C,r*c,xc,yc)


recursive_tree(n,90,r,10,5)