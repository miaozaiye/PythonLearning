#计算随机冲浪情况下，每个页面的最终被访问概率
'''
用户在页面i上，随机访问链接j的概率为 p[i][j]
实现方式：
1. 基于转化概率生成数值区间：sp[j] = sum(p[i][h],h in range(j+1)
2. 通过random.random 随机生成概率浮点数 x, x落在哪个sp[j-1]~sp[j]区间，则相当于随机跳转到j

操作流程：

1.输入跳转总次数n
2. 从页面0开始
3. 随机生成概率 sp，根据sp跳转到下一个页面，对于被跳转到的页面计数
4。重复3，直到总次数耗尽
5。输出每个页面被跳转到的比例（次数／n)

'''

from stdpackage import stdio,stdarray,stddraw
import random
import sys

moves = int(sys.argv[1])
n = stdio.readInt()
stdio.readInt()
P = stdarray.create2D(n,n,0.0)
P_accumulated = stdarray.create2D(n,n,0.0)
SP = stdarray.create1D(n,0.0)


for i in range(n):
    for j in range(n):
        P[i][j] = stdio.readFloat()
for i in range(n):
    for j in range(n):
        for h in range(j+1):
            P_accumulated[i][j] +=P[i][h]

def find_page(i,p):
    j=0
    while j <n:
        if p < P_accumulated[i][j]:
            return j
        else:
            j +=1
    pass
move_count = 0
i = 0
while move_count<moves:
    p = random.random()
    j = find_page(i,p)
    SP[j] +=1
    i = j
    move_count+=1

for i in range(n):
    stddraw.clear()

    stdio.writef('%5.2f',SP[i])
    stdio.writeln()



