
import sys
sys.path.insert(0,'/Users/Jane/Library/Python/3.5/lib/python/site-packages/')
from stdpackage import stdio,instream,stdrandom,stdarray
import time
import random
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




def doubletrial(f,n,trials):
    timelist = stdarray.create1D(5)
    for i in range(5):
        timelist[i] = trialtime(f,n*(2**i),trials)
        print(n*(2**i),trials,timelist[i]/timelist[0])


doubletrial(insert,128,100)