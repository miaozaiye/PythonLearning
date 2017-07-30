#验证对于一个1-6点的骰子而言，每投掷6次，至少出现1次1，每投掷12次，至少出现2次1。

'''
altorithm:


for i in range(12):
    a = random.randrange(1,6)
    count if a==1

    if i ==5:
        result = true if count>=1 else false
        result1.append(result)
        print( result )
    if i == 11:
        result = true if count >=2 else false
        result2.append(result)
        print (result)


'''

import random
import optparse
import time

def PepysProblem():
    time_start = time.time()
    result1 = []
    result2 = []
    n = 1
    while n<100:
        result = 0
        for i in range (12):
            a = random.randrange(6)
            result += (1 if a ==1 else 0)
            if i == 5:
                print('result in 6 times :{0}'.format(result))
                result1.append(True if result >= 1 else False)
            if i ==11:
                result2.append(True if result >= 2 else False)
                print('result in 12 times :{0}'.format(result))
        n+=1
    print('The possibility of scenario 1 is {0}%, of scenario 2 is {1}%'.format(
        result1.count(True),result2.count(True)))

    time_end = time.time()
    time_delta = time_end-time_start
    print('time elapsed {0}'.format(time_delta))
PepysProblem()