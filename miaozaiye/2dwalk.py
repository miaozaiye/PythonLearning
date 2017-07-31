#给定输入N，看点 P 从原点开始随机往4个方向走，什么时候能走到2N* 2N 的边界
'''
algorithm:

UP,DOWN,LEFT,RIGHT = 1,-1,1j,-1j
p = 0+0j
choice=dict(0 = UP,1 = DOWN,2 = LEFT,3 = RIGHT)
step = 0
while True:
    step +=1
    change = choice[random.randrange(4)]
    a +=change

    if (a.real == 2*N or a.imag ==2*N):
        print('step is {0}'.format(step)
        break
'''

import random
import optparse

def TwoDWalk(n):
    UP,DOWN,LEFT,RIGHT = 1,-1,1j,-1j
    p = 0+0j
    choice={0:UP, 1:DOWN, 2: LEFT,3:RIGHT}
    step = 0

    while True:
        step +=1
        change = choice[random.randrange(4)]
        p +=change
        print('change is {0}, point is at ({1},{2})'.format(change,p.real,p.imag))

        if (p.real == 2*n or p.imag ==2*n):
            print('step is {0}'.format(step))
            break


def main():
    '''

    帮助信息
    获取参数


    '''


    parser = optparse.OptionParser("""\
usage: %prog [options] infile outfile

tell you how mant random steps it takes to achieve the border of 2n*2n square,
n is your input number.
""")

    parser.add_option("-n", "--number", dest="number",
            help=("input the number, to get the steps"))
    opts, args = parser.parse_args()
    TwoDWalk(int(opts.number))


main()