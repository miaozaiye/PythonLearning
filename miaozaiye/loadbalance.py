#实现负载均衡
'''
1. 有N个任务，M台服务器，每次取样T
2。 每次随机选取T台服务器，对比寻找其中队列最短的，部署（增加）任务。

'''
import sys
sys.path.insert(0,'/Users/Jane/Library/Python/3.5/lib/python/site-packages/')
sys.path.insert(0,'/Users/Jane/Desktop/PythonLearning')

from miaozaiye.randomqueue import RandomQueue
from miaozaiye.nodequene import link
from stdpackage import stdstats,stddraw,stdarray

M = 5
N = 500
T = 3
servicegroup = RandomQueue()

for i in range(M):
    servicegroup.enqueue(list())

Length = stdarray.create1D(M,0)
for i in range(N):
    best = servicegroup.sample()
    print("object {0}".format(i))
    for randomtry in range(T-1):
        queue = servicegroup.sample()
        print('find random queue:',queue)
        if len(best) > len(queue):
            best = queue
    best.append(i)

    a = 0
    for list in servicegroup.queue():
        Length[a]=len(list)
        a+=1
    stddraw.clear()
    stddraw.setYscale(-1,70)
    stdstats.plotBars(Length)
    stddraw.show(100)

print('end')
for list in servicegroup.queue():
    print(list)


