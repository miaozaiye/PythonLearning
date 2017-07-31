#给定任意一个整数a，找到 0-a 之间满足 A^3 + B^3 = C^3 +D^3, 其中ABCD都是正整数。

'''
altorithm:

对于小于n的整数a,
拆分a成两个立方的和:

for a in range(n)
j = a - i^3 for i in range(1,a^(1/3))
if j^(1/3) is int, record.

if record >1, count and record.

'''
import optparse


def ramanuian_taxi(n):
    assert n >=1729,'the number must be bigger than 1729'
    record = {}
    for a in range(1729,n+1):
        b = []
        c = []
        for i in range(0,round((a/2)**(1/3))):

            j = (a-i**3)**(1/3)

            if abs(j-round(j))<0.000001:

                b.append((i,round((a - i**3)**(1/3))))
        record[a]=b

    for key in record:
        if len(record[key])>1:
            print(key,record[key])


def main():
    '''

    帮助信息
    获取参数


    '''


    parser = optparse.OptionParser("""\
usage: %prog [options] infile outfile

tell you the RamanujansNumber that in range(0,your input)

if int1^3 + int2^3 = int3^3+int4^3 = a, then we call a 'RamanujansNumber""")

    parser.add_option("-n", "--number", dest="number",
            help=("get the RamanujansNumber sequence"))
    opts, args = parser.parse_args()
    ramanuian_taxi(int(opts.number))


main()