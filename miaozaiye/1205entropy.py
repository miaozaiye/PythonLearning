#信息熵公式 sum(-p_c log(2,p_c)
'''
1。从标准输入读取字符串
2。计算字符串的信息熵
3。从标准输出输出熵值

'''
from stdpackage import stdio
import math

def possibility(c,s):
    count = 0
    for i in s:
        if i == c:
            count+=1
    return count/len(s)

def count_entropy(s):
    sum = 0
    for c in s:
        p = possibility(c,s)
        sum -=p*math.log(p,2)
    return sum

def main():
    print('please input your information:')
    s = stdio.readLine().strip('/n')
    entropy_sum = 0.0


    entropy_sum =count_entropy(s)

    stdio.writeln('The engropy of "{0}" is {1}'.format(s,entropy_sum))


main()