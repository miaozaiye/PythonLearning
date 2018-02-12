
import sys
sys.path.insert(0,'/Users/Jane/Library/Python/3.5/lib/python/site-packages/')
from stdpackage import stdio,instream,stdrandom,stdarray,stddraw
import time
import random
sys.path.insert(0,'/Users/Jane/Desktop/PythonLearning')
import pygame

from miaozaiye import merge


def exchange(a,j):
    a[j],a[j-1] = a[j-1],a[j]



def insert(a):

    for i in range(0,len(a)):
        j = i

        while j >0 and a[j] < a[j-1]:
            exchange(a,j)

            j-=1


class stopwatch():
    def __init__(self):
        self._start = time.time()

    def elapsedTime(self):
        return time.time() - self._start



def trialtime(f,n,trials):
    '''
    1. generate random list with length n
    2. start time
    3. sort f with list(n)
    4. end time

    :param f:
    :param n:
    :return: time
    '''

    List = stdarray.create1D(n,0)
    total = 0
    for i in range(len(List)):
        List[i] = random.randint(0,1000)

    for t in range(trials):
        watch =stopwatch()
        f(List)

        total +=watch.elapsedTime()
    averagetime = total/trials

    return averagetime




def doubletrial(f,n,length,trials):
    timelist = stdarray.create1D(length)
    timecount = stdarray.create1D(length)
    for i in range(length):
        timelist[i] = trialtime(f,n*(2**i),trials)

        print(n*(2**i),timelist[i],int(timelist[i]/timelist[0]))
        timecount[i] = int(timelist[i]/timelist[0])
    return timelist

def draw_count(countlist):
    # stddraw.setCanvasSize(100,100)
    stddraw.setXscale(-1,10)
    stddraw.setYscale(-0.1,0.5)
    stddraw.setPenColor(stddraw.GRAY)
    stddraw.line(0,0,100,0)
    stddraw.line(0,0,0,5000)
    for List in countlist:
        for i in range(1,len(List)):
            stddraw.line(i-1,List[i-1],i,List[i])


def main(length,trials):


    count1 = doubletrial(insert,30,length,trials)
    count2 = doubletrial(merge.insert,30,length,trials)
    print(count1,'\n',count2)

    draw_count([count1,count2])
    stddraw.show()

main(10,100)

