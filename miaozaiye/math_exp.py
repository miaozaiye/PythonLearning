#用4种方式计算 e^x，并计算各种方式的时间消耗。

'''
algorithm:

泰勒展开：
e^x = 1+x+x^2/2+x^3/3!+x^4/4!+......


方法1：直接用math.exp() 函数


方法2：
num = 1.0
den = 1.0
for i in range(1,n+1):
    num*=x

for i in range(1,n+1):
    den*=i
term =num/den

total+ = term


方法3：

term = 1.0
total = 0.0

while total != total + term:
    total+=term
    term = 1.0
    for i in range(1,n+1):
        term*=x/i
    n+=1


方法4：

term=1.0
total= 0.0
n = 1
while total != total + term:
    total +=term
    term *=x/n
    n+=1
'''

import time
import math
import optparse

def exp_time(x):

    #方法1的结果和耗时
    time1_start=time.time()
    result = math.exp(x)
    time1_end = time.time()
    time1_delta = time1_end - time1_start
    print ('method 1:\n result is {0},time elapsed {1}'.format(result,time1_delta))

    #方法2
    time2_start = time.time()

    total = 1
    term =1
    n_1 = 1
    while total !=total + term:
        num = 1.0
        den = 1.0
        for i in range(1,n_1+1):
            num*=x

        for i in range(1,n_1+1):
            den*=i

        term =num/den

        total += term

        n_1+=1

    time2_end = time.time()
    time2_delta = time2_end - time2_start
    print('method 2:\n result is {0},time elapsed {1}'.format(total,time2_delta))

    #方法3
    time3_start = time.time()

    total = 1.0
    term =1.0
    n_2 = 1
    while total !=total + term:
        term = 1
        for i in range(1,n_2+1):
            term *=x/i
        total += term
        n_2+=1

    time3_end = time.time()
    time3_delta = time3_end - time3_start
    print('method 3:\n result is {0},time elapsed {1}'.format(total,time3_delta))

     #方法4
    time4_start = time.time()
    total = 1.0
    term =1.0
    i = 1


    while total !=total + term:
        term *=x/i
        total +=term
        i+=1


    time4_end = time.time()
    time4_delta = time4_end - time4_start
    print('method 4:\n result is {0},time elapsed {1}'.format(total,time4_delta))


def main():
    '''

    帮助信息
    获取参数


    '''


    parser = optparse.OptionParser("""\
usage: %prog [options] infile outfile

tell you result of e^x(x is your input) via 4 methods,
and how much time it takes in each way""")

    parser.add_option("-e", "--exp", dest="exp",
            help=("get the exp"))
    opts, args = parser.parse_args()
    exp_time(float(opts.exp))


main()

