#计算输出转换矩阵，矩阵上第i行第j列的数字，代表从i页跳转到 j页的概率

from stdpackage import stdarray,stdio

n = stdio.readInt()

linkCounts = stdarray.create2D(n,n,0)
outDegress = stdarray.create1D(n,0)

while not stdio.isEmpty():
    i = stdio.readInt()

    j = stdio.readInt()
    outDegress[i]+=1
    linkCounts[i][j] +=1

stdio.writeln(str(n)+' '+str(n))

for i in range(n):
    for j in range(n):
        p = (0.9*linkCounts[i][j]/outDegress[i])+(0.1/n)
        stdio.writef('%8.5f',p)
    stdio.writeln()