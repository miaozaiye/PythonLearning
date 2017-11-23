#估计概率

import sys
from stdpackage import stddraw,stdio
from miaozaiye.percolation import percolationv,percolationio

def evaluate(n,p,trials):
    count = 0
    for i in range(trials):
        isOpen = percolationio.random(n,p)
        if (percolationv.percolates(isOpen)):
            count +=1

    return 1.0* count/trials


def main():
    n = 5
    p = 0.5
    trials = 2000

    q = evaluate(n,p,trials)
    stdio.writeln(q)


main()