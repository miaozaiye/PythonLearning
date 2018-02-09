#通过二分查找法，猜出神秘数字

'''
1. 指定数字范围[lo_0,hi_0]
2. 每次询问数字是否包含在半封闭空间 [hi_(i-1)/2，hi_i)
3. 是，则在该空间继续第2步
4. 不是，则询问是否包含在半封闭空间 [lo_(i-1),hi_(i-1)/2)

'''

import sys

hi_0 = 300

print('think about a number in [0,{0})'.format(300))

def guess(lo,hi):
    print('lo is {0},hi is {1}'.format(lo,hi))

    if hi - lo == 1:
        print('enter if')
        print ('lo is:',lo)
        return lo

    else:
        print('enter else')
        mid = int((hi-lo)/2+lo)

        choice = input('is your number in [{0},{1})?(y/n)'.format(mid,hi))
        if choice =='y':
            guess(mid,hi)
        if choice =='n':
            guess(lo,mid)


number = guess(0,hi_0)
print('number is :{0}'.format(number))