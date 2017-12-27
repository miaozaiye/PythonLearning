#create a stopwatch with test client

import math
import sys
import time
from stdpackage import stdio

class stopwatch():
    def __init__(self):
        self._start = time.time()

    def elapsedTime(self):
        return time.time() - self._start

def main():
    n = int(sys.argv[1])

    total1 = 0.0
    watch1 = stopwatch()
    for i in range(n):
        total1 +=i**2

    time1 = watch1.elapsedTime()

    total2 = 0.0
    watch2 = stopwatch()
    for i in range(n):
        total2 += i*i
    time2 = watch2.elapsedTime()

    stdio.writeln(total1/total2)
    stdio.writeln(time1/time2)

if __name__ == '__main__': main()