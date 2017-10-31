#dice 1: 1,3,4,5,6,8   dice 2:1,2,2,3,3,4

'''
比较这两个骰子和两个标准骰子的点数和各值出现的几率

'''

import sys
import random
from stdpackage import stdrandom,stdstats,stddraw,stdarray

def dice(dice_1,dice_2,n):
    index = []

    for i in range(6):
        for j in range(6):
            if dice_1[i] + dice_2[j] not in index:
                index.append(dice_1[i]+dice_2[j])
        else:
            pass

    result = stdarray.create1D(len(index),0)
    for i in range(n):
        sum = dice_1[stdrandom.uniformInt(0,5)] + dice_2[stdrandom.uniformInt(0,5)]
        result[sum]+=1


    return result


def run(n):

    dice_1 = [1,3,4,5,6,8]
    dice_2 = [1,2,2,3,3,4]
    dice_s = [1,2,3,4,5,6]

    result1 = dice(dice_1,dice_2,n)
    result2 = dice(dice_s,dice_s,n)

    print(result1,result2)


    stddraw.setYscale(0,1.1*max(max(result1),max(result2)))
    stdstats.plotLines(result1)
    stdstats.plotBars(result2)
    stddraw.show(50)

stddraw.setCanvasSize(1000,400)
for n in range(50,200):
    stddraw.clear()
    run(n)