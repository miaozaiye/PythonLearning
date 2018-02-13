#模拟MM1队列，比如考虑，高速公路汽车通过收费站的情况。

'''
1。两种类型事物：
   1）用户随机到达
   2）用户服务，处理时间固定

2。两个变量：
    1）下一个用户到达时间
    2）服务下一个用户的时间

3。单位时间内到达人数和服务人数，和平均每个人等待时间的关系

'''

import sys
from stdpackage import stddraw,stdarray,stdrandom,stdstats
from miaozaiye import nodequene
import random


#0 create 2 data class: visit,service

#1 generate lamda random float number in 1 unit time


#2 inqueue those time in visit.arrival


#3 for No.x's service, service start time = max(last service end, current arrival, service end time = start time + miu

#4 visit.pass = service end time, visit wait = visit.pass - visit.arrival

#5 count the average visit.wait time with the given lamda and miu

#7 run the count with different lamda and miu ,draw square picture to show the relationship


class Histogram:
    def __init__(self,n):
        self._freq = stdarray.create1D(n,0)

    def addDataPoint(self,i):
        self._freq[i] +=1

    def draw(self):
        stddraw.setYscale(0,max(self._freq))
        stdstats.plotBars(self._freq)


histogram = Histogram(60+1)

def count_waittime(lamda,miu):
    print('enter count_waittime')

    queue = nodequene.link()
    time = []
    a = 0
    nextarrival = stdrandom.exp(lamda)
    nextservice = nextarrival+stdrandom.exp(miu)

    print(nextarrival,nextservice)
    while a<100:

        while nextarrival<nextservice:
            nextarrival +=stdrandom.exp(lamda)
            queue.inqueue(nextarrival)
            print('{0} in queue'.format(queue.last.item))

        arrival = queue.outqueue()
        print(nextservice,arrival)
        waittime = nextservice - arrival
        time.append(waittime)

        stddraw.clear()
        histogram.addDataPoint(min(60,int(round(waittime))))
        histogram.draw()
        stddraw.show(20)


        if queue.isempty():
            nextservice = nextarrival + stdrandom.exp(miu)

        else:
            nextservice = nextservice +stdrandom.exp(miu)

        a+=1




    return time

def gen_frequencylist(datasource):
    datasource.sort()
    a = datasource[0]
    b = datasource[-1]
    delta = (b-a)/20
    count = stdarray.create1D(20,0)
    j = 0
    for i in range(1,20):

        while datasource[j]<a+delta*i:

            j+=1
            count[i]+=1
        i+=1

    print(count)
    return count



def draw_square(datasource):
    '''
    drawpicture
    :param datasource:
    :return:
    '''
    print('enter draw_square')
    stddraw.setPenColor(stddraw.BLACK)
    stddraw.setXscale(-0.1,len(datasource))
    stddraw.setYscale(-1,20)
    stddraw.line(0,0,len(datasource),0)
    stddraw.line(0,0,0,20)

    frequency_list = gen_frequencylist(datasource)

    for x,y in enumerate(frequency_list):
        stddraw.rectangle(x-1,0,1,y)

        # stddraw.text(x,y+1,'x:{0:.2f}   y:{1:.2f}'.format(x,y))

    stddraw.show()




def main(L_lamda_miu):

    datasource = []

    waittime = count_waittime(L_lamda_miu[0],L_lamda_miu[1])
    draw_square(waittime)


L_lamda_miu = [0.5,0.2]
#
# print(L_lamda_miu)
# for i in range(20):
#     print('i is {0:.2f}'.format(i))
#     L_lamda_miu[i][0] = random.randint(1,100)
#     L_lamda_miu[i][1] = random.randint(1,100)

main(L_lamda_miu)



