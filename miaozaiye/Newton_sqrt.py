#count sqrt via newton iteration
'''
算法：
对于曲线f(x)=0,如果一阶导函数f_nd(x)存在，可以利用牛顿迭代来快速求得近似解。

对于初次预估近似解 x_0, 有切线方程：y-f(x_0)=(x-x_0)*f_nd(x_0)
真实解对应于 y = 0, x = x_n
(x_n -  x_(n-1))f_nd(x_0) + f(x_(n-1))=0

x_n = x_(n-1) - f(x_(n-1))/f_nd(x_(n-1))
当 x_n - x(n-1) < 指定误差时，我们认为x_n 是可以接受的近似值


对于求a 的 平方根而言，则方程如下：

f(x) = x**2 - a
f_nd(x) = 2x
x_0 = a
x = x_(n-1)-((x_(n-1))**2-a)/2(x_(n-1))

'''

import optparse
import sys
Epsilon = 1e-15


def Newton_sqrt(c):

    t = c
    while abs(t - c/t)>Epsilon:

        t = (c/t + t)/2.0


    print('the sqrt of {0} is {1:.5f}'.format(c,t))



def main():
    '''

    帮助信息
    获取参数


    '''


    parser = optparse.OptionParser("""\
usage: %prog [options] infile outfile

tell you the sqrt of your input number""")

    parser.add_option("-r", "--sqrt", dest="sqrt",
            help=("get the sqrt"))
    opts, args = parser.parse_args()
    Newton_sqrt(float(opts.sqrt))


main()