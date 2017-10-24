#混合马尔可夫链
'''
接受命令行参数 moves，从标准输入读取一个转换矩阵（浮点数），通过moves次向量-矩阵乘法计算，计算
一个随机冲浪者经过moves步跳转到达各页面的概率。
最后在标准输出中输出页面排名

命令行模式：
python3 tansition.py<tiny.txt|python3 markov.py 20
'''

from stdpackage import stdio,stdarray
import sys

moves = int(sys.argv[1])
n = stdio.readInt()
stdio.readInt()

p = stdarray.create2D(n,n,0.0)
for i in range(n):
    for j in range(n):
        p[i][j] = stdio.readFloat()

ranks = stdarray.create1D(n,0.0)

ranks[0] = 1.0
for i in range(moves):
    new_ranks = stdarray.create1D(n,0.0)
    for k in range(n):
        for j in range(n):
         new_ranks[j] += ranks[k]*p[k][j]
    ranks = new_ranks

for i in range(n):
    stdio.writef('%8.5f',ranks[i])
stdio.writeln()

