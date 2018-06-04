import sys
sys.path.insert(0,'/Users/Jane/Library/Python/3.5/lib/python/site-packages/')
sys.path.insert(0,'/Users/Jane/Desktop/PythonLearning')

import pygame
import time

from stdpackage import stdio,stddraw

class stopwatch():
    def __init__(self):
        self._start = time.time()

    def elapsedTime(self):
        return time.time() - self._start

def main():
    duration = int(input('what is the duration?(min):'))
    status = input('start to work?(Y/N)')

    while status == 'Y':
        stddraw.clear()
        stddraw.setXscale(0,10)
        stddraw.setYscale(0,10)
        time.sleep(duration * 60)
        stddraw.text(5,5,'go to do sport')
        stddraw.show()
        status = input('continue to work?(Y/N')
        if status == 'N':
            break

main()
# if __name__ == '__main__': main()