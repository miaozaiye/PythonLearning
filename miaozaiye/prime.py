#本程序根据输入，计算所有小于等于输入的素数并返回明细，以及个数
'''
algorithm:

素数定义： 只能被 和本身整除的数，如：2，3，5，7，11，43。。。。

for i in range(1,n):
    for j in range(2,i/2):
        left = i%j
        if left ==0:
            tag = 0
            break
    if tag !=0:
        prime_list.append(i)



'''

import optparse

def prime(n):
    prime_list = [1]
    left = 0

    for index in range(2,n+1):
        tag = 1


        for j in range(2,index+1):

            left = index%j

            if left == 0 and j not in [1,index]:
                tag = 0



        if tag == 1:
            prime_list.append(index)

    print(len(prime_list),prime_list)


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
    prime(int(opts.number))


main()