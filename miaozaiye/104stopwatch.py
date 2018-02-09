#创建一个检测程序运行时间的对象，可以记录现在的时间，已过去的时间。

import time
import sys
from stdpackage import stdarray
from miaozaiye import bouncingball


class Watchstop:
    def __init__(self):
        self._now =time.time()

    def starttime(self):
        return self._now

    def elapsedtime(self):
        return time.time()-self._now


def main():

    n = int(sys.argv[1])

    for i in range(n):
        time1 = Watchstop()
        L = stdarray.create1D(i)

        print (time1.elapsedtime())


    # time2 = Watchstop()
    # for i in range(n):
    #     i
    #     print(i)
    # print(time1.elapsedtime()/time2.elapsedtime())

if __name__ == '__main__': main()