import sys
import random
from stdpackage import stdarray,stddraw,stdrandom,stdstats
import math
from miaozaiye import gaussian

# n = int(sys.argv[1])
# trials = int(sys.argv[2])

n= 20
trials = 10000
p = 0.1
stddraw.setCanvasSize(1000,400)

for n in range(20,1000):

    stddraw.clear()
    freq = stdarray.create1D(n+1,0)

    for t in range(trials):
        heads = stdrandom.binomial(n,0.7)
        freq[heads] +=1

    norm = stdarray.create1D(n+1,0)
    for i in range(n+1):
        norm[i] = 1.0*freq[i]/trials

    phi = stdarray.create1D(n+1,0.0)
    stddev = math.sqrt(n)/2.0

    for i in range(n+1):
        phi[i] = gaussian.pdf(i,n/2.0,stddev)

    stddraw.setYscale(0,1.1*max(max(norm),max(phi)))
    stdstats.plotBars(norm)
    stdstats.plotLines(phi)
    stddraw.show(20)