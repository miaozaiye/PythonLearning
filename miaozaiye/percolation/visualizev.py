import sys
from stdpackage import stddraw
sys.path.append('/Users/Jane/Desktop/PythonLearning/miaozaiye/percolation')
from miaozaiye.percolation import percolationio,percolationv

n = 20
p = 0.9
trials = 3

for i in range(trials):
    isOpen = percolationio.random(n,p)
    stddraw.clear()
    stddraw.setPenColor(stddraw.BLACK)
    percolationio.draw(isOpen,False)
    stddraw.setPenColor(stddraw.BLUE)
    isFull = percolationv.flow(isOpen)
    percolationio.draw(isFull,True)
    stddraw.show(1000.0)

stddraw.show()


