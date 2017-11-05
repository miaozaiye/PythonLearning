#学习递归思路寻找最大公约数
'''
gcd(p,q) = gcd(q,p%q)

'''

import sys
a = int(sys.argv[1])
b = int(sys.argv[2])

(p,q) = (a,b) if a>b else (b,a)

def gcd(p,q):
    if p%q == 0:
        return q
    return gcd(q,p%q)

print(gcd(p,q))