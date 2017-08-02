#通过厄拉多塞素数筛选法来筛选所有小于用户输入的N的素数

'''
algorithm

设置布尔数组 isPrime = ['True'...]
只要满足i<N:
查找下一个最小的素数
保持isPrime[i]为True
将索引下表为i的整数倍的isPrime[]所有数组元素的值都设为False


'''

import optparse

def primesieve(n):
    isPrime = ['True']*(n+1)
    for i in range(2,n+1):
        if isPrime[i] == False:
            pass
        else:
            for j in range(i,int(n/i+1)):
                print ('i is {0},j is {1}'.format(i,j))
                isPrime[i*j] = False

    print(isPrime)
    prime = []
    for index,value in enumerate(isPrime):
        print(index,value)
        if value=='True':
            print(index,value)
            prime.append(index)


    print(prime)
    number = len(prime)-1
    print(number)


def main():
    '''

    帮助信息
    获取参数


    '''


    parser = optparse.OptionParser("""\
usage: %prog [options] infile outfile

tell you the prime numbers that in range(0,your input)
""")

    parser.add_option("-n", "--number", dest="number",
            help=("get the prime number sequence"))
    opts, args = parser.parse_args()
    primesieve(int(opts.number))


main()
