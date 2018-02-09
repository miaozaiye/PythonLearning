#通过插入法对随机数组进行排序

'''
1.外循环i从0到len(list)
2.内循环j从 i 到1
3。对比内循环下标位置的对象和前一个对象，如果小于前一个，则兑换位置。

'''

import sys
sys.path.insert(0,'/Users/Jane/Library/Python/3.5/lib/python/site-packages/')
from stdpackage import stdio,instream

#exchange location

def exchange(a,j):
    a[j],a[j-1] = a[j-1],a[j]



def insert(a):

    for i in range(0,len(a)):
        j = i

        while j >0 and a[j] < a[j-1]:
            exchange(a,j)

            j-=1

def main():
    inst =instream.InStream(sys.argv[1])
    a = inst.readAllStrings()
    print(a)
    insert(a)
    print(a)

if __name__ == '__main__':main()

